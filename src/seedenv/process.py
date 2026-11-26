"""Argument arrays and bounded, cancellable installer processes."""
from contextlib import contextmanager
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


class Cancelled(Exception):
    pass


def stop(process):
    if process.poll() is not None:
        return
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        if process.poll() is None:
            process.kill()
    else:
        try:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=3)
        except ProcessLookupError:
            pass
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
    process.wait()


def run(command, *, env=None, cancel=None, timeout=1800, cwd=None):
    if cancel and cancel.exists():
        raise Cancelled("Preparation cancelled")
    process = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=sys.stderr,
                               stderr=sys.stderr, env=env, cwd=cwd, start_new_session=os.name != "nt")
    start = time.monotonic()
    try:
        while process.poll() is None:
            if cancel and cancel.exists():
                raise Cancelled("Preparation cancelled")
            if time.monotonic() - start > timeout:
                raise TimeoutError("Preparation exceeded its time limit")
            time.sleep(0.1)
        if process.returncode:
            raise RuntimeError(f"{Path(command[0]).name} exited with status {process.returncode}; see preparation output")
    except BaseException:
        stop(process)
        raise


@contextmanager
def installation_lock(path, *, wait=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+b") as handle:
        # Do not read byte zero before locking it: Windows forbids reading a
        # region already held by another preparer.
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK if wait else msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle, fcntl.LOCK_EX if wait else fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise RuntimeError("This component is being prepared by another process") from error
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle, fcntl.LOCK_UN)
