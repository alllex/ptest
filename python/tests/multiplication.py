
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

from test import PythonTest, get_data, int_data, long_data

# -------------------------------------------------------
#                     Multiplication Tests
# -------------------------------------------------------

class Multiplication(PythonTest):

    @staticmethod
    def object(): return 'Python multiplication operator'

    @staticmethod
    def test(a, b):
        return a * b

class MultiplicationOfInt(Multiplication): # int considered here as having (2**31 - 1) max value

    @staticmethod
    def name(): return 'Multiplication of ints'

    @staticmethod
    def params():
        return int_data(get_data('MultiplicationOfInt'))

class MultiplicationOfLong(Multiplication): # long considered here as having (2**63 - 1) max value

    @staticmethod
    def name(): return 'Multiplication of longs'

    @staticmethod
    def params():
        return long_data(get_data('MultiplicationOfLong'))

class MultiplicationOfBigInt(Multiplication):

    @staticmethod
    def name(): return 'Multiplication of big ints'

    @staticmethod
    def params():
        return long_data(get_data('MultiplicationOfBigInt'))