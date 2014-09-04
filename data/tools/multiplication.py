
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

# -------------------------------------------------------
#              Data for multiplication tests
# -------------------------------------------------------

def MultiplicationOfInt(): # int considered here as having (2**31 - 1) max value
    data = [
        (1, 0),
        (1, 1),
        (3, -5),
        (101, 42),
        (42, 101),
        (1<<10,1<<20),
        ((1<<10) - 1,(1<<20) - 1),
        (24851, 27751)
    ]
    return map(lambda (a, b): (int(a), int(b)), data)

def MultiplicationOfLong(): # long considered here as having (2**63 - 1) max value
    data = [
        (1, 0),
        (1, 1),
        (3, -5),
        (1<<10,1<<20),
        (2702765, 199360981),
        (2**30, 2**30 - 1)
    ]
    return map(lambda (a, b): (long(a), long(b)), data)

def MultiplicationOfBigInt():
    data = [
        (1, 0),
        (1, 1),
        (3, -5),
        (2**127, 3**42),
        (7**70 - 2**20, 5**80 - 2**21),
    ]
    return map(lambda (a, b): (long(a), long(b)), data)