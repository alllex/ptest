#!/bin/bash

if [ $PTEST == "TRUE" ]; then

    if [ ! -d "$GEN" ]; then
      mkdir "$GEN"
    fi

    PREFS_FILE="$GEN/$PREFS"

    # if [ ! -f "$PREFS_FILE" ] ; then
    #     touch "$PREFS_FILE"
    # fi

    echo "$REPEAT_FAST" >"$PREFS_FILE"
    echo "$REPEAT_MID" >>"$PREFS_FILE"
    echo "$REPEAT_SLOW" >>"$PREFS_FILE"

    echo "$NUMBER_FAST" >>"$PREFS_FILE"
    echo "$NUMBER_MID" >>"$PREFS_FILE"
    echo "$NUMBER_SLOW" >>"$PREFS_FILE"

fi