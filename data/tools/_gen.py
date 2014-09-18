
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04


# -------------------------------------------------------
#                     Print utils
# -------------------------------------------------------

folder_name = 'gen'
file_ext = '.data'

def create_folder(folder_name):
    import os
    if not os.path.exists(folder_name): os.makedirs(folder_name)

def create_filename(test_name):
    from os.path import join
    return join(folder_name, test_name + file_ext)

def print_samples(data_function):
    filename = create_filename(data_function.__name__)
    data = data_function()
    with open(filename, 'w+') as f: 
        for sample in data:
            for piece in sample:
                f.write('%s ' % str(piece)) 
            f.write('\n')
    
# -------------------------------------------------------
#                 Grouped data for tests
# -------------------------------------------------------

from addition import *
from factorial import *
from factorialbig import *
from gcd import *
from loop import *
from multiplication import *
from string import *

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
    FactorialBig,

    Loop
]

# -------------------------------------------------------
#                 Grouped data for tests
# -------------------------------------------------------

def main():
    create_folder(folder_name)
    for s in all_samples: print_samples(s)

if __name__ == '__main__':
    main()