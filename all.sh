#!/bin/bash

# Run all tests

RES=results
GEN=gen

cd data
. ./gen.sh

cd ..
if [ ! -d "$RES" ]; then
  mkdir "$RES"
fi

echo Run all tests

# Python
. ./python/run.sh

echo All tests successfully finished