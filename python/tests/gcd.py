
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

from test import PythonTest
        
# -------------------------------------------------------
#                     GCD Tests
# -------------------------------------------------------

class GCD(PythonTest):

    @staticmethod
    def object(): return 'gcd(a, b)'

    @staticmethod
    def params():
        data = [
            (2, 3),
            (1, 1),
            (5, 3),
            (42, 101),
            (1<<10,1<<20),
            ((1<<10) - 1,(1<<20) - 1),
            (2**30, 2**30 - 1),
            (2702765, 199360981), # primes
            (196418, 317811)      # fibonacci numbers
        ]
        return map(lambda (a, b): (int(a), int(b)), data)

class GCDByFractionsLib(GCD):

    @staticmethod
    def name(): return 'GCD from fractions library'

    @staticmethod
    def test((a, b)):
        from fractions import gcd
        return gcd(a, b)

class GCDByRecursiveImpl(GCD):

    @staticmethod
    def name(): return 'GCD by recursive implementation'

    @staticmethod
    def test((a, b)):
        def gcd(a, b):
            if b == 0: return a 
            else: return gcd(b, a % b)
        return gcd(a, b)

class GCDByLoopImpl(GCD):

    @staticmethod
    def name(): return 'GCD by while-loop implementation'

    @staticmethod
    def test((a, b)):
        def gcd(a, b):
            while b != 0:
                t = b
                b = a % b
                a = t
            return a
        return gcd(a, b)