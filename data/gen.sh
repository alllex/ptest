#!/bin/bash

# Generate data for tests

if [ $PTEST == "TRUE" ]; then

    echo Start generating data for tests

    if [ ! -d "$GEN" ]; then
      mkdir "$GEN"
    fi

    python --version 2>/dev/null
    if [ $? -eq 0 ]; then
        python "tools/_gen.py"
        if [ $? -eq 0 ]; then
            echo "Data successfully generated"
        else
            echo "Error occured during data generation"
        fi
    else
        echo "Python isn't installed"
        echo "Install Python and add it to PATH"
    fi
    
fi