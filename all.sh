#!/bin/bash

# Run all tests

PTEST=TRUE
RES=results
GEN=gen
PREFS=prefs.data
TEST_FAILED=FALSE

. ./prefs.sh

cd data
. ./gen.sh

cd ..
if [ ! -d "$RES" ]; then
  mkdir "$RES"
fi

echo Run all tests

# Python
# . ./python/run.sh

# Perl
. ./perl/run.sh

if [ ! $TEST_FAILED == "TRUE" ]; then
    echo "All tests successfully finished"
fi