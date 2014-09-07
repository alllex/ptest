#!/bin/bash

if [ $PTEST == "TRUE" ]; then

    python --version 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Run Python tests..."
        python "python/ptest-python.py"
        if [ $? -eq 0 ]; then
            echo "Python tests successfully finished"
        else
            echo "Error occured during testing"
            TEST_FAILED=TRUE
        fi
    else
        echo "Python isn't installed"
        echo "Install Python and add it to PATH"
        TEST_FAILED=TRUE
    fi
fi