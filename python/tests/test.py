
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

class Test:
    @staticmethod
    def name(): pass
    @staticmethod
    def subject(): pass
    @staticmethod
    def object(): pass
    @staticmethod
    def test(param): pass
    @staticmethod
    def params(): pass

class PythonTest(Test):
    @staticmethod
    def subject():
        import sys
        return 'python-%s' % (sys.version.split()[0])