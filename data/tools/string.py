
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

# -------------------------------------------------------
#                 Data for string tests
# -------------------------------------------------------

def StringEquals():
    alphabet100 = "abcdefghijklmnoprstuvwxyz" * 100
    data = [
        ("xxx", "xxx"),
        ("abc" * 100, "abc" * 99 + "axc"),
        (alphabet100, alphabet100[:]),
        (alphabet100, alphabet100[:] + "!"),
        (alphabet100 + "?", alphabet100[:] + "!"),
        (alphabet100 + "?" + alphabet100[:], alphabet100[:] + "!" + alphabet100[:])
    ]
    return map(lambda (a, b): (str(a), str(b)), data)

def StringConcat():
    alphabet100 = "abcdefghijklmnoprstuvwxyz" * 100
    data = [
        ("abc" * 100, ""),
        ("", "abc" * 100),
        ("xxx", "xxx"),
        (alphabet100, alphabet100[:]),
        (alphabet100, alphabet100[:] + "!"),
        (alphabet100 + "?", alphabet100[:] + "!"),
        (alphabet100 + "?" + alphabet100[:], alphabet100[:] + "!" + alphabet100[:])
    ]
    return map(lambda (a, b): (str(a), str(b)), data)

def StringFind():
    alphabet = "abcdefghijklmnoprstuvwxyz"
    alphaZ = "xyZ"
    alphabet100 = alphabet * 100
    data = [
        ("abc" * 100, ""),
        ("", "abc" * 100),
        ("xxx", "xxx"),
        (alphabet100, alphabet),
        (alphabet100, alphaZ),
        (alphabet100 + "?", "!"),
        (alphabet100 + "?" + alphabet100[:], "?")
    ]
    return map(lambda (a, b): (str(a), str(b)), data)

def StringReplace():
    alphabet = "abcdefghijklmnoprstuvwxyz"
    alphaZ = "xyZ"
    alphabet100 = alphabet * 100
    data = [
        ("abc" * 100, "abc", "xxx"),
        ("abc" * 100, "abca", "xxx"),
        ("abc" * 100, "abcx", "xxx"),
        ("", "abc" * 100, "x"),
        ("xxx", "xxx", "xxx"),
        (alphabet100 + "?", "!", "x"),
        (alphabet100 + "?" + alphabet100[:], "?", "x")
    ]
    return map(lambda (s, old, new): (str(s), str(old), str(new)), data)