#!/bin/bash

# Run Perl tests

LANG=perl
EXT=pl

if [ $PTEST == "TRUE" ]; then

    $LANG --version >/dev/null
    if [ $? -eq 0 ]; then
        echo "Run $LANG tests..."
        $LANG "$LANG/ptest-$LANG.$EXT"
        if [ $? -eq 0 ]; then
            echo "$LANG tests successfully finished"
        else
            echo "Error occured during testing"
            TEST_FAILED=TRUE
        fi
    else
        echo "$LANG isn't installed"
        echo "Install $LANG and add it to PATH"
        TEST_FAILED=TRUE
    fi
fi