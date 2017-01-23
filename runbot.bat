TITLE LapisMirror
@ECHO off

CHCP 65001 > NUL
CD /d "%~dp0"

IF EXIST %SYSTEMROOT%\py.exe (
    CMD /k py.exe -3.5 lapis.py
    EXIT
)

python --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO nopython

CMD /k python lapis.py
GOTO end


:nopython
ECHO ERROR: Python has either not been installed or not added to your PATH.

:end
PAUSE
