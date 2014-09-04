
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

from test import PythonTest, get_data, int_data

# -------------------------------------------------------
#                     Loop Tests
# -------------------------------------------------------

class Loop(PythonTest):

    @staticmethod
    def object(): return 'loop(0, n - 1)'

    @staticmethod
    def params():
        return int_data(get_data('Loop'))

class LoopByXRange(Loop):

    @staticmethod
    def name(): return 'Loop using xrange'

    @staticmethod
    def test(n):
        tmp = True
        for i in xrange(n):
            tmp = not tmp # light operation for loop body

class LoopByRange(Loop):

    @staticmethod
    def name(): return 'Loop using range'

    @staticmethod
    def test(n):
        tmp = True
        for i in range(n):
            tmp = not tmp # light operation for loop body

class LoopByWhile(Loop):

    @staticmethod
    def name(): return 'Loop using while'

    @staticmethod
    def test(n):
        tmp = True
        i = 0
        while i < n:
            i += 1        # as part of loop implementation
            tmp = not tmp # light operation for loop body