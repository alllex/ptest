
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

from test import PythonTest

# -------------------------------------------------------
#                     String Tests
# -------------------------------------------------------

class StringEquals(PythonTest):

    @staticmethod
    def object(): return 's1 == s2'

    @staticmethod
    def name(): return 'Equals string'

    @staticmethod
    def test((s1, s2)):
        return s1 == s2

    @staticmethod
    def params():
        alphabet100 = "abcdefghijklmnoprstuvwxyz" * 100
        data = [
            ("", ""),
            ("abc" * 100, ""),
            ("", "abc" * 100),
            ("xxx", "xxx"),
            (alphabet100, alphabet100[:]),
            (alphabet100, alphabet100[:] + "!"),
            (alphabet100 + "?", alphabet100[:] + "!"),
            (alphabet100 + "?" + alphabet100[:], alphabet100[:] + "!" + alphabet100[:])
        ]
        return map(lambda (a, b): (str(a), str(b)), data)

class StringConcat(PythonTest):

    @staticmethod
    def object(): return 's1 + s2'

    @staticmethod
    def name(): return 'String concatenation'

    @staticmethod
    def test((s1, s2)):
        return s1 + s2

    @staticmethod
    def params():
        alphabet100 = "abcdefghijklmnoprstuvwxyz" * 100
        data = [
            ("", ""),
            ("abc" * 100, ""),
            ("", "abc" * 100),
            ("xxx", "xxx"),
            (alphabet100, alphabet100[:]),
            (alphabet100, alphabet100[:] + "!"),
            (alphabet100 + "?", alphabet100[:] + "!"),
            (alphabet100 + "?" + alphabet100[:], alphabet100[:] + "!" + alphabet100[:])
        ]
        return map(lambda (a, b): (str(a), str(b)), data)

class StringFind(PythonTest):

    @staticmethod
    def object(): return 's.find(p)'

    @staticmethod
    def name(): return 'find() from string library'

    @staticmethod
    def test((s, pattern)):
        return s.find(pattern)

    @staticmethod
    def params():
        alphabet = "abcdefghijklmnoprstuvwxyz"
        alphaZ = "xyZ"
        alphabet100 = alphabet * 100
        data = [
            ("", ""),
            ("abc" * 100, ""),
            ("", "abc" * 100),
            ("xxx", "xxx"),
            (alphabet100, alphabet),
            (alphabet100, alphaZ),
            (alphabet100 + "?", "!"),
            (alphabet100 + "?" + alphabet100[:], "?")
        ]
        return map(lambda (a, b): (str(a), str(b)), data)

class StringReplace(PythonTest):

    @staticmethod
    def object(): return 's.replace(old, new)'

    @staticmethod
    def name(): return 'replace() from string library'

    @staticmethod
    def test((s, old, new)):
        return s.replace(old, new)

    @staticmethod
    def params():
        alphabet = "abcdefghijklmnoprstuvwxyz"
        alphaZ = "xyZ"
        alphabet100 = alphabet * 100
        data = [
            ("", "", ""),
            ("abc" * 100, "abc", "xxx"),
            ("abc" * 100, "abca", "xxx"),
            ("abc" * 100, "abcx", "xxx"),
            ("", "abc" * 100, "x"),
            ("xxx", "xxx", "xxx"),
            (alphabet100 + "?", "!", "x"),
            (alphabet100 + "?" + alphabet100[:], "?", "x")
        ]
        return map(lambda (s, old, new): (str(s), str(old), str(new)), data)