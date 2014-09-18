#!/bin/bash

if [ $PTEST == "TRUE" ]; then

    REPEAT_FAST=1
    REPEAT_MID=1
    REPEAT_SLOW=1

    NUMBER_FAST=1000000
    NUMBER_MID=100000
    NUMBER_SLOW=1000

    cd data
    . ./prefs.sh
    cd ..

fi