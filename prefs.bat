
:: Preferences

IF "%PTEST%"=="" GOTO :EOF

SET REPEAT_FAST=10
SET REPEAT_MID=10
SET REPEAT_SLOW=10

SET NUMBER_FAST=1000000
SET NUMBER_MID=100000
SET NUMBER_SLOW=1000

CD data
CALL prefs.bat
CD ..
