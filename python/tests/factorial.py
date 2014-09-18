
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

class FactorialByRec(Factorial):

    @staticmethod
    def name(): return 'Factorial by recursive implementation'

    @staticmethod
    def test(n):
        def factorial(n):
            if n == 0: return 1
            else: return n * factorial(n - 1)
        return factorial(n)

class FactorialByLoop(Factorial):

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

class FactorialBig(PythonTest):
    @staticmethod
    def object(): return 'factorial(n)'

    @staticmethod
    def params():
        return int_data(get_data('FactorialBig'))

class FactorialBigByMathLib(FactorialBig):

    @staticmethod
    def name(): return 'FactorialBig from math library'

    @staticmethod
    def test(n):
        from math import factorial
        return factorial(n)

class FactorialBigByRec(FactorialBig):

    @staticmethod
    def name(): return 'FactorialBig by recursive implementation'

    @staticmethod
    def test(n):
        def factorial(n):
            if n == 0: return 1
            else: return n * factorial(n - 1)
        return factorial(n)

class FactorialBigByLoop(FactorialBig):

    @staticmethod
    def name(): return 'FactorialBig by while-loop implementation'

    @staticmethod
    def test(n):
        def factorial(n):
            r = 1
            while n > 0:
                r *= n
                n -= 1
            return r
        return factorial(n)