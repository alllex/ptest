
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

def get_data(test_name):
    # def splitn(a, n): return zip(*[a[i::n] for i in range(n)])
    from os.path import join
    file_ext = '.data'
    file_path = join('data', 'gen', test_name + file_ext)
    with open(file_path) as f:
        # size = int(f.readline())
        samples = [tuple(line.split()) for line in f]
    return samples

def cast_data(data, cast_item):
    return list(map(lambda pieces: 
            tuple(map(lambda item: cast_item(item), pieces))
        , data))

def int_data(data):
    return cast_data(data, int)

def long_data(data):
    return cast_data(data, long)

def str_data(data):
    return cast_data(data, str)
