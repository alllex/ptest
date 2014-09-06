#!/bin/bash

python --version 2>/dev/null
if [ $? -eq 0 ]; then
    echo "Run Python tests..."
    python "python/ptest-python.py"
    if [ $? -eq 0 ]; then
        echo "Python tests successfully finished"
    else
        echo "Error occured during testing"
    fi
else
    echo "Python isn't installed"
    echo "Install Python and add it to PATH"
fi
