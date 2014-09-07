#!/bin/bash

# Clear

RES=results
GEN=data/gen

if [ -d "$RES" ]; then
    rm -rf "$RES"
fi

if [ -d "$GEN" ]; then
    rm -rf "$GEN"
fi

