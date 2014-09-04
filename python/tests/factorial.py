
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

from test import PythonTest, get_data, int_data

# -------------------------------------------------------
#                     Factorial Tests
# -------------------------------------------------------

class Factorial(PythonTest):
    @staticmethod
    def object(): return 'factorial(n)'

    @staticmethod
    def params():
        return int_data(get_data('Factorial'))

class FactorialByMathLib(Factorial):

    @staticmethod
    def name(): return 'Factorial from math library'

    @staticmethod
    def test(n):
        from math import factorial
        return factorial(n)

class FactorialByRecursiveImpl(Factorial):

    @staticmethod
    def name(): return 'Factorial by recursive implementation'

    @staticmethod
    def test(n):
        def factorial(n):
            if n == 0: return 1
            else: return n * factorial(n - 1)
        return factorial(n)

class FactorialByLoopImpl(Factorial):

    @staticmethod
    def name(): return 'Factorial by while-loop implementation'

    @staticmethod
    def test(n):
        def factorial(n):
            r = 1
            while n > 0:
                r *= n
                n -= 1
            return r
        return factorial(n)