@echo off
set /p filename="Filename: "

pyinstaller -F --onefile --icon=icon.ico "%filename%"