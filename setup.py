from __future__ import annotations

from cx_Freeze import setup, Executable
import sys, os, typing

include_files = [(os.path.join("Resources", "FavIcon.png"), "Resources/FavIcon.png")]

base: typing.Any = None
if sys.platform == "win32": base = "Win32GUI"

setup(name="EtoMazhor", version="2025.2",
    description="Opa opa eto mazhor, yeah",
    options={
        "build_exe": { "packages": ["tkinter", "os"], "include_files": include_files, "excludes": ["unnecessary_module"], }
    }, executables=[Executable("Window.py", base=base)],)
