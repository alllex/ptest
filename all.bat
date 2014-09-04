
:: Run all tests

@echo off

SET RES=results
SET GEN=gen

CD data
CALL gen.bat

CD ..
IF NOT EXIST %RES% MD %RES%

ECHO Run all tests

:: Python
CALL "python/run.bat"

ECHO All tests successfully finished

