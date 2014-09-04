
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

# -------------------------------------------------------
#                Data for addition tests
# -------------------------------------------------------

def AdditionOfInt():
    data = [
        (1, 0),
        (1, 1),
        (3, -5),
        (101, 42),
        (42, 101),
        (1<<10,1<<20),
        ((1<<10) - 1,(1<<20) - 1),
        (2**30, 2**30 - 1),
        (2702765, 199360981)
    ]
    return map(lambda (a, b): (int(a), int(b)), data)

def AdditionOfLong():
    data = [
        (1, 0),
        (1, 1),
        (3, -5),
        (1<<10,1<<20),
        (2702765, 199360981),
        (2**62, 2**62 - 1),
        (2**42, 2**42 - 2**21)
    ]
    return map(lambda (a, b): (long(a), long(b)), data)
       
def AdditionOfBigInt():
    data = [
        (1, 0),
        (1, 1),
        (3, -5),
        (2**127, 3**42),
        (7**70 - 2**20, 5**80 - 2**21)
    ]
    return map(lambda (a, b): (long(a), long(b)), data)