
:: Run all tests

@echo off

SET PTEST=TRUE
SET RES=results
SET GEN=gen
SET PREFS=prefs.data
SET TEST_FAILED=FALSE

CALL prefs.bat

CD data
CALL gen.bat
IF ERRORLEVEL 1 GOTO :EOF
CD ..

IF NOT EXIST %RES% MD %RES%

ECHO Run all tests

:: Python
CALL "python/run.bat"

:: Perl
:: CALL "perl/run.bat"

IF "%TEST_FAILED" == "FALSE" (
    ECHO All tests successfully finished
)

