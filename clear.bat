
:: Clear

@echo off

SET RES=results
SET GEN=data\gen

IF EXIST %RES% RMDIR /s /q %RES%

IF EXIST %GEN% RMDIR /s /q %GEN%