
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

from test import PythonTest, get_data, str_data

# -------------------------------------------------------
#                     String Tests
# -------------------------------------------------------

class StringEquals(PythonTest):

    @staticmethod
    def object(): return 's1 == s2'

    @staticmethod
    def name(): return 'Equals string'

    @staticmethod
    def test(s1, s2):
        return s1 == s2

    @staticmethod
    def params():
        return str_data(get_data('StringEquals'))

class StringConcat(PythonTest):

    @staticmethod
    def object(): return 's1 + s2'

    @staticmethod
    def name(): return 'String concatenation'

    @staticmethod
    def test(s1, s2):
        return s1 + s2

    @staticmethod
    def params():
        return str_data(get_data('StringConcat'))

class StringFind(PythonTest):

    @staticmethod
    def object(): return 's.find(p)'

    @staticmethod
    def name(): return 'find() from string library'

    @staticmethod
    def test(s, pattern):
        return s.find(pattern)

    @staticmethod
    def params():
        return str_data(get_data('StringFind'))

class StringReplace(PythonTest):

    @staticmethod
    def object(): return 's.replace(old, new)'

    @staticmethod
    def name(): return 'replace() from string library'

    @staticmethod
    def test(s, old, new):
        return s.replace(old, new)

    @staticmethod
    def params():
        return str_data(get_data('StringReplace'))