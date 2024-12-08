from __future__ import annotations

from cx_Freeze import setup, Executable
import sys, os

include_files = [(os.path.join('resources', 'favicon.png'), "resources/favicon.png")]

base = None
if sys.platform == "win32": base = "Win32GUI"

setup(
    name="EtoMazhor",
    version="2024.1",
    description="Opa opa eto mazhor, yeah",
    options={
        "build_exe": {
            "packages": ["tkinter", "os"], "include_files": include_files, "excludes": ["unnecessary_module"],
        }
    },
    executables=[Executable("window.py", base=base)],
)
