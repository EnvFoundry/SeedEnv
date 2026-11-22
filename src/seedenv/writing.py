"""Build an existing LaTeX project without putting intermediates in its delivery.

    seedenv build manuscript/main.tex --output deliverables/paper.pdf

Requires latexmk and LuaLaTeX (default) or XeLaTeX on PATH. --latexmk can select
a prepared TeX installation; its bin directory is also used for child tools.
Sources stay in their original project. TeX logs, dependency records and all
other build products stay in --build-dir (default: <source directory>/build).
Only a successful PDF is copied to --output (default: beside the source).
The command prints a JSON result and exits nonzero on failure; it does not
install packages, clean build records or change the source project.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess

from .catalog import DATA


def templates(language=None, form=None, style=None):
    """List small layout descriptions; no installation or project writes."""
    path = DATA / "writing" / "templates.json"
    if not path.is_file():
        return {"items": []}
    items = json.loads(path.read_text(encoding="utf-8"))
    return {"items": [item for item in items if
                      (language is None or item["language"] == language) and
                      (form is None or item["form"] == form) and
                      (style is None or item["style"] == style)]}


def create_manuscript(template, output):
    """Copy a selected editable project, independently of Python/TeX setup."""
    item = next((t for t in templates()["items"] if t["id"] == template), None)
    if item is None:
        raise ValueError(f"Unknown writing template: {template}")
    target = Path(output).expanduser().absolute()
    target.mkdir(parents=True, exist_ok=False)
    try:
        shutil.copy2(DATA / "writing" / item["file"], target / "main.tex")
        for asset in item["assets"]:
            shutil.copy2(DATA / "writing" / asset, target / Path(asset).name)
        (target / "figures").mkdir()
        # A comment-only bibliography would make BibTeX fail on an empty project.
        # Create refs.bib when the manuscript has actual references.
        (target / "README.md").write_text(
            "# Manuscript / 文稿\n\nEdit main.tex; put figures in figures/. "
            "Add actual references to refs.bib when needed.\n"
            "编辑 main.tex，图表放入 figures/；需要引用时添加真实的 refs.bib。\n\n"
            f"Build / 编译：`seedenv build main.tex --engine {item['engine']}`\n\n"
            "This layout is editable. Follow the chosen venue's current requirements.\n"
            "这是可编辑的排版起点；投稿时按目标期刊的实际要求调整。\n", encoding="utf-8")
    except BaseException:
        shutil.rmtree(target)
        raise
    return {"template": template, "path": str(target), "source": str(target / "main.tex"),
            "engine": item["engine"], "build": ["seedenv", "build", str(target / "main.tex"), "--engine", item["engine"]]}


def build_manuscript(
    source: Path,
    *,
    build_dir: Path | None = None,
    output: Path | None = None,
    engine: str = "lualatex",
    latexmk: str = "latexmk",
    environment: dict[str, str] | None = None,
) -> dict[str, object]:
    source = source.expanduser().resolve()
    if source.suffix.lower() != ".tex" or not source.is_file():
        raise ValueError(f"LaTeX entry file not found: {source}")
    if engine not in ("lualatex", "xelatex"):
        raise ValueError("engine must be lualatex or xelatex")
    build = (build_dir or source.parent / "build").expanduser().resolve()
    if build == source.parent:
        raise ValueError("build directory must be separate from the source directory")
    destination = (output or source.with_suffix(".pdf")).expanduser().resolve()
    if destination.suffix.lower() != ".pdf":
        raise ValueError("output must be a .pdf file")

    executable = shutil.which(os.path.expanduser(latexmk))
    if not executable:
        raise FileNotFoundError(f"latexmk executable not found: {latexmk}")
    # Do not resolve symlinks: TeX installations often dispatch by executable name.
    executable = os.path.abspath(executable)
    env = {**os.environ, **(environment or {})}
    env["PATH"] = str(Path(executable).parent) + os.pathsep + env.get("PATH", "")
    if not shutil.which(engine, path=env["PATH"]):
        raise FileNotFoundError(f"{engine} not found beside latexmk or on PATH")

    build.mkdir(parents=True, exist_ok=True)
    # Older latexmk needs standard TeX diagnostics to create nested include aux dirs.
    command = [
        executable, f"-{engine}", "-g", "-interaction=nonstopmode", "-halt-on-error",
        f"-outdir={build.as_posix()}", f"./{source.name}",
    ]
    transcript = build / f"{source.stem}.latexmk.log"
    log = build / f"{source.stem}.log"
    pdf = build / f"{source.stem}.pdf"
    with transcript.open("w", encoding="utf-8") as stream:
        stream.write(json.dumps({"cwd": str(source.parent), "command": command}) + "\n")
        stream.flush()
        completed = subprocess.run(
            command, cwd=source.parent, env=env, stdout=stream,
            stderr=subprocess.STDOUT, check=False,
        )
    result: dict[str, object] = {
        "status": "failed", "returncode": completed.returncode,
        "source": str(source), "build_dir": str(build), "engine": engine,
        "command": command, "log": str(log), "transcript": str(transcript),
    }
    if completed.returncode != 0:
        result["error"] = "latexmk failed; inspect the retained log and transcript"
    elif not pdf.is_file() or pdf.stat().st_size == 0:
        result["returncode"] = 1
        result["error"] = "latexmk returned success without a nonempty PDF"
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination != pdf:
            shutil.copy2(pdf, destination)
        result.update(status="built", pdf=str(destination))
    return result

