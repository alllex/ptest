
:: Run python tests

@echo off

python --version 2>NUL
IF ERRORLEVEL 1 GOTO NOPYTHON 

ECHO Run Python tests...
python.exe "python\ptest-python.py"
IF ERRORLEVEL 1 GOTO GENERROR
ECHO Python tests successfully finished
GOTO :EOF

:GENERROR
ECHO Error occured during testing
PAUSE
GOTO :EOF

:NOPYTHON
ECHO Python isn't installed
ECHO Install Python and add it to PATH
PAUSE
GOTO :EOF