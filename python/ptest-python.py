
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

from tests.test import *
from tests.addition import *
from tests.multiplication import *
from tests.loop import *
from tests.gcd import *
from tests.factorial import *
from tests.string import *

# -------------------------------------------------------
#                     Benchmark utils
# -------------------------------------------------------

def benchmark(test_name, module_name, repeat=1, number=1):
    from timeit import repeat as benchmarker
    setup = 'from tests.%s import %s' % (module_name, test_name)
    test_func = test_name + '.test'
    params = eval(test_name + '.params()')
    timed = []
    for param in params:
        sample = '%s(*%s)' % (test_func, param)
        best_time = min(benchmarker(sample, setup=setup, repeat=repeat, number=number))
        timed.append((best_time, param))
    return (
        test_name,
        repeat,
        number,
        timed
    )

def now():
    from time import strftime
    from datetime import datetime
    return datetime.now()

def mk_logname(test_name): 
    folder = 'results'
    lang = PythonTest.subject()
    ext  = 'log'
    return '%s/%s-%s.%s' % (folder, test_name, lang, ext)

def tool_name():
    import sys
    return 'Python: %s' % sys.version

def log_benchmark(bench_args):
    from datetime import datetime
    start_time = datetime.now()
    test_name, rep, num, timed = benchmark(*bench_args)
    finish_time = datetime.now()
    diff = str(finish_time - start_time)
    logname = mk_logname(test_name)

    with open(logname, 'a') as log:
        repeat = '{:^3}'.format(rep)
        number = '{:^9}'.format(num)
        test_name = '{:^20}'.format(test_name)

        log.write('{0}\n'.format(tool_name()))
        to_log = 'Test case({t}): repeat({r}) of number({n})\nAll {count} tests took about {total} to process'.format(
            t=test_name, r=repeat, n=number, total=diff, count='{:^3}'.format(len(timed))
        )
        log.write(to_log + "\n")
        print(to_log)

        for bt, p in timed:
            to_log = '{bt} // {p}'.format(bt='{:0.5f}'.format(bt), p=p)
            log.write(to_log + "\n")

# -------------------------------------------------------
#                   Test compilation
# -------------------------------------------------------

def tests():

    fast = [

        ('addition', [
                'AdditionOfInt', 
                'AdditionOfLong', 
                'AdditionOfBigInt'
            ]
        ),

        ('multiplication', [
                'MultiplicationOfInt', 
                'MultiplicationOfLong', 
                'MultiplicationOfBigInt'
            ]
        ),

        ('gcd', [
                'GCDByFractionsLib', 
                'GCDByRecursiveImpl', 
                'GCDByLoopImpl'
            ]
        ),

        ('string', [
                'StringEquals', 
                'StringConcat', 
                'StringFind',
                'StringReplace'
            ]
        )
    ]
    mid = [

        ('loop', [
                'LoopByXRange', 
                'LoopByRange', 
                'LoopByWhile'
            ]
        ),

        ('factorial', [
                'FactorialByMathLib', 
                'FactorialByRecursiveImpl', 
                'FactorialByLoopImpl'
            ]
        )
    ]
    slow = [
    ]

    def mk_bunch(repeat, number, (module_name, test_classes)):
        return [(t, module_name, repeat, number) for t in test_classes]

    prefs = get_prefs()
    repeat_fast = prefs[0]
    repeat_mid  = prefs[1]
    repeat_slow = prefs[2]
    number_fast = prefs[3]
    number_mid  = prefs[4]
    number_slow = prefs[5]

    tests = []
    for t in fast: tests += mk_bunch(repeat_fast, number_fast, t)
    for t in mid: tests += mk_bunch(repeat_mid, number_mid, t)
    for t in slow: tests += mk_bunch(repeat_slow, number_slow, t)
    return tests # tuples - (test class, module name, repeat times, runs per test)

# -------------------------------------------------------
#                     Test runner
# -------------------------------------------------------

def main():
    for t in tests(): log_benchmark(t)

if __name__ == '__main__':
    main()


