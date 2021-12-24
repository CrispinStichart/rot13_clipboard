#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; ctrl-alt-P -- you can change this to whatever.
^!p::
    ; Note the use of pythonw to prevent a console window from appearing.
    Run, .\venv\Scripts\pythonw.exe rot13.py
    return