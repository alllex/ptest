
:: Generate data for tests

@echo off

IF "%PTEST%"=="" GOTO :EOF

ECHO Start generating data for tests

IF NOT EXIST %GEN% MD %GEN%

python --version 2>NUL
IF ERRORLEVEL 1 GOTO NOPYTHON 

python "tools\_gen.py"
IF ERRORLEVEL 1 GOTO GENERROR
ECHO Data successfully generated
GOTO :EOF

:GENERROR
ECHO Error occured during data generation
GOTO :EOF

:NOPYTHON
ECHO Python isn't installed
ECHO Install Python and add it to PATH
GOTO :EOF