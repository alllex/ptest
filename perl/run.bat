
:: Run python tests

@echo off

SET LANG=perl
SET EXT=pl

%LANG% --version >NUL
IF ERRORLEVEL 1 GOTO NOPYTHON 

ECHO Run %LANG% tests...
%LANG% "%LANG%\ptest-%LANG%.%EXT%"
IF ERRORLEVEL 1 GOTO GENERROR
ECHO %LANG% tests successfully finished
GOTO :EOF

:GENERROR
ECHO Error occured during testing
SET TEST_FAILED=TRUE
GOTO :EOF

:NOPYTHON
ECHO %LANG% isn't installed
ECHO Install %LANG% and add it to PATH
SET TEST_FAILED=TRUE
GOTO :EOF