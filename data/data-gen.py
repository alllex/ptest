
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04


# -------------------------------------------------------
#                     Print utils
# -------------------------------------------------------

file_ext = '.data'

def create_filename(test_name):
    return test_name + file_ext

def print_samples(data_function):
    filename = create_filename(data_function.__name__)
    data = data_function()
    with open(filename, 'w+') as f: 
        f.write('%s\n' % len(data[0]))
        for sample in data:
            for piece in sample:
                f.write('%s\n' % str(piece)) 
    
# -------------------------------------------------------
#                 Grouped data for tests
# -------------------------------------------------------

from tests.addition import *
from tests.factorial import *
from tests.gcd import *
from tests.loop import *
from tests.multiplication import *
from tests.string import *

all_samples = [

    AdditionOfInt,
    AdditionOfLong,
    AdditionOfBigInt,

    GCD,

    MultiplicationOfInt,
    MultiplicationOfLong,
    MultiplicationOfBigInt,

    StringEquals,
    StringConcat,
    StringFind,
    StringReplace,

    Factorial,

    Loop
]

# -------------------------------------------------------
#                 Grouped data for tests
# -------------------------------------------------------

def main():
    for s in all_samples: print_samples(s)

if __name__ == '__main__':
    main()