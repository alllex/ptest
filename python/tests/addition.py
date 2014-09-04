
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

# -------------------------------------------------------
#                     Addition Tests
# -------------------------------------------------------

from test import PythonTest, get_data, int_data, long_data

class Addition(PythonTest):

    @staticmethod
    def object(): return 'Python addition operator'

    @staticmethod
    def test(a, b):
        return a + b

class AdditionOfInt(Addition): # int considered here as having (2**31 - 1) max value

    @staticmethod
    def name(): return 'Addition of ints'

    @staticmethod
    def params():
        return int_data(get_data('AdditionOfInt'))

class AdditionOfLong(Addition): # long considered here as having (2**63 - 1) max value

    @staticmethod
    def name(): return 'Addition of longs'

    @staticmethod
    def params():
        return long_data(get_data('AdditionOfLong'))

class AdditionOfBigInt(Addition):

    @staticmethod
    def name(): return 'Addition of big ints'

    @staticmethod
    def params():
        return long_data(get_data('AdditionOfBigInt'))