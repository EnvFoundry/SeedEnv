"""Portable TeX preparation shared by standalone clients and product workers.

The native archive and package selection are adapted from Origo's research-tex
preparer. TeX stays upstream; SeedEnv supplies a location and invocation entries.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tarfile
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from zipfile import BadZipFile, ZipFile

from .catalog import DATA
from .process import Cancelled, installation_lock, run


def recipe():
    return json.loads((DATA / "tex.json").read_text(encoding="utf-8"))


def asset_name(system=None, machine=None):
    system = system or platform.system()
    arch = (machine or platform.machine()).lower()
    if system == "Windows" and arch in {"amd64", "x86_64"}:
        target, extension = "windows", "exe"
    elif system == "Darwin" and arch in {"arm64", "aarch64", "x86_64", "amd64"}:
        target, extension = "darwin", "tar.xz"
    elif system == "Linux" and arch in {"arm64", "aarch64", "x86_64", "amd64"}:
        arch = "arm64" if arch in {"arm64", "aarch64"} else "x86_64"
        target, extension = "linux-" + arch, "tar.xz"
        if platform.libc_ver()[0] == "musl":
            if arch != "x86_64":
                raise ValueError("Connect an installed TeX toolchain on Linux musl ARM64")
            target = "linuxmusl-x86_64"
    else:
        raise ValueError(f"Connect an installed TeX toolchain on {system} {arch}")
    return f"TinyTeX-1-{target}-v{recipe()['release']}.{extension}"


def _cancelled(cancel):
    if cancel and cancel.exists():
        raise Cancelled("Preparation cancelled")


def _download(url, path, cancel=None):
    """Retain a partial archive and continue only when the server honors Range."""
    if path.is_file():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_suffix(path.suffix + ".partial")
    offset = partial.stat().st_size if partial.exists() else 0
    headers = {"Range": f"bytes={offset}-"} if offset else {}
    print(f"Downloading {path.name}", file=sys.stderr, flush=True)
    _cancelled(cancel)
    try:
        response = urlopen(Request(url, headers=headers), timeout=30)
    except HTTPError as error:
        if error.code != 416 or not offset:
            raise
        # Cancellation may happen after the final byte but before the rename.
        complete = error.headers.get("Content-Range") == f"bytes */{offset}"
        error.close()
        if complete:
            _cancelled(cancel)
            partial.replace(path)
            return
        response = urlopen(Request(url), timeout=30)
    with response:
        append = offset and response.status == 206
        if append and not response.headers.get("Content-Range", "").startswith(f"bytes {offset}-"):
            raise RuntimeError("Download server returned an unexpected byte range; retry preparation")
        expected = response.headers.get("Content-Length")
        received = 0
        with partial.open("ab" if append else "wb") as stream:
            while True:
                _cancelled(cancel)
                block = response.read(1024 * 1024)
                if not block:
                    break
                stream.write(block)
                received += len(block)
        if expected is not None and received != int(expected):
            raise RuntimeError("TeX download interrupted; retry preparation to continue")
    _cancelled(cancel)
    partial.replace(path)


def environment(home, command):
    """Supply TeX child programs and writable caches without changing user PATH."""
    root = Path(home) / "tex-state"
    return {"PATH": str(Path(command[0]).parent) + os.pathsep + os.environ.get("PATH", ""),
            "TEXMFHOME": str(root / "home"), "TEXMFVAR": str(root / "var"),
            "TEXMFCONFIG": str(root / "config"), "TEXMFCACHE": str(root / "var")}


def describe(command):
    """An existing latexmk alone is not the required compiler and font set."""
    if len(command) != 1:
        raise ValueError("Use the actual latexmk executable on this execution host")
    search = str(Path(command[0]).parent) + os.pathsep + os.environ.get("PATH", "")
    programs = {"latexmk": command[0]}
    for name in ("lualatex", "xelatex", "pdflatex", "bibtex", "kpsewhich"):
        program = shutil.which(name, path=search)
        if not program:
            raise ValueError(f"Existing TeX is missing {name}; connect a complete installation or prepare writing")
        programs[name] = str(Path(program).absolute())
    env = {**os.environ, "PATH": search}
    version = subprocess.run([programs["latexmk"], "-v"], stdin=subprocess.DEVNULL,
                             capture_output=True, env=env, timeout=15)
    if version.returncode or b"latexmk" not in (version.stdout + version.stderr).lower():
        raise ValueError("The selected command is not a working latexmk")
    biber = shutil.which("biber", path=search)
    if biber:
        programs["biber"] = str(Path(biber).absolute())
    for resource in ("ctexart.cls", "FandolSong-Regular.otf"):
        result = subprocess.run([programs["kpsewhich"], resource], stdin=subprocess.DEVNULL,
                                capture_output=True, env=env, timeout=15)
        if result.returncode or not result.stdout.strip():
            raise ValueError(f"Existing TeX is missing {resource}; add it upstream or prepare writing")
    return programs


def find_existing():
    program = shutil.which("latexmk")
    if program:
        command = [str(Path(program).absolute())]
        try:
            describe(command)
            return command
        except (OSError, ValueError, subprocess.TimeoutExpired):
            pass
    return None


def _install_fonts(root, cache, fonts, bin_dir, env, cancel):
    local = root / "texmf-local"
    for font in fonts:
        archive = cache / f"{font['id']}-{font['version']}.zip"
        _download(font["url"], archive, cancel)
        try:
            with ZipFile(archive) as bundle:
                for source, relative in font["files"].items():
                    _cancelled(cancel)
                    destination = local / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    temporary = destination.with_suffix(destination.suffix + ".partial")
                    with bundle.open(source) as content, temporary.open("wb") as target:
                        shutil.copyfileobj(content, target)
                    temporary.replace(destination)
        except (BadZipFile, KeyError) as error:
            raise RuntimeError(f"Cannot install {font['id']} fonts from {font['url']}: {error}") from error
    suffix = ".exe" if os.name == "nt" else ""
    run([str(bin_dir / ("mktexlsr" + suffix)), str(local)], env=env, cwd=bin_dir, cancel=cancel)


def prepare(home, *, offline=False, cancel=None):
    """Prepare a user-owned TinyTeX without modifying any existing TeX install."""
    home = Path(home)
    spec = recipe()
    asset = asset_name()
    root = home / "software" / asset.removesuffix(".tar.xz").removesuffix(".exe")
    complete = root / "seedenv-prepared.json"
    with installation_lock(home / "locks" / "tool-tex.lock"):
        if complete.is_file():
            saved = json.loads(complete.read_text(encoding="utf-8"))
            command = [str(root / saved["latexmk"])]
            describe(command)
            return command, root
        if offline:
            raise ValueError("TeX is not prepared here; connect an existing installation or prepare once online")
        if os.name != "nt" and shutil.which("perl") is None:
            raise ValueError("TinyTeX needs Perl on this execution host; install the platform's Perl first")
        root.parent.mkdir(parents=True, exist_ok=True)
        archive = home / "cache" / asset
        _download(f"https://github.com/rstudio/tinytex-releases/releases/download/v{spec['release']}/{asset}", archive, cancel)
        staging = root.parent / ("." + root.name + ".preparing")
        if not root.exists():
            # Extraction can be repeated from the completed local archive.
            if staging.exists():
                shutil.rmtree(staging)
            staging.mkdir()
            _cancelled(cancel)
            if os.name == "nt":
                run([str(archive), "-y", "-o" + str(staging)], cwd=staging, cancel=cancel)
            else:
                with tarfile.open(archive) as bundle:
                    bundle.extractall(staging, filter="data")
            installations = [p for p in staging.iterdir() if (p / "bin").is_dir()]
            if len(installations) != 1:
                raise RuntimeError("Cannot locate TinyTeX in its archive")
            installations[0].replace(root)
            shutil.rmtree(staging)
        bins = [p for p in (root / "bin").iterdir() if p.is_dir()]
        if len(bins) != 1:
            raise RuntimeError("TinyTeX must contain one native program directory")
        bin_dir = bins[0]
        suffix = ".exe" if os.name == "nt" else ""
        command = [str(bin_dir / ("latexmk" + suffix))]
        env = dict(os.environ)
        for key in list(env):
            if key.startswith("TEXMF") or key in {"TEXINPUTS", "BIBINPUTS", "BSTINPUTS"}:
                del env[key]
        env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")
        # The Windows launcher completes self-updates after Perl exits. Calling
        # tlmgr.pl directly leaves that update unfinished. A relative batch name
        # keeps the installation's spaces out of cmd.exe's command text.
        manager = ([os.environ.get("COMSPEC", "cmd.exe"), "/d", "/c", r".\tlmgr.bat"]
                   if os.name == "nt" else [str(bin_dir / "tlmgr")])
        for args in (["option", "repository", spec["repository"]], ["option", "docfiles", "0"],
                     ["option", "srcfiles", "0"], ["update", "--self"],
                     ["install", *spec["packages"]]):
            _cancelled(cancel)
            run([*manager, *args], env=env, cwd=bin_dir, cancel=cancel)
        _install_fonts(root, home / "cache", spec["fonts"], bin_dir, env, cancel)
        run([*manager, "postaction", "install", "script", "xetex"], env=env, cwd=bin_dir, cancel=cancel)
        describe(command)
        for folder in ("home", "var", "config"):
            (home / "tex-state" / folder).mkdir(parents=True, exist_ok=True)
        _cancelled(cancel)
        complete.write_text(json.dumps({"latexmk": str(Path(command[0]).relative_to(root)),
                                        "fonts": spec["fonts"]}) + "\n", encoding="utf-8")
        return command, root
