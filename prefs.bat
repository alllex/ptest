
:: Preferences

IF "%PTEST%"=="" GOTO :EOF

SET REPEAT_FAST=1
SET REPEAT_MID=1
SET REPEAT_SLOW=1

SET NUMBER_FAST=1000000
SET NUMBER_MID=10000
SET NUMBER_SLOW=100

CD data
CALL prefs.bat
CD ..