
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

def benchmark(module_name, test_name, repeat, number):
    from timeit import repeat as benchmarker
    setup = 'from tests.%s import %s' % (module_name, test_name)
    test_func = test_name + '.test'
    params = eval(test_name + '.params()')
    timed = []
    for param in params:
        sample = '%s(*%s)' % (test_func, param)
        best_time = min(benchmarker(sample, setup=setup, repeat=repeat, number=number))
        res = eval(sample)
        timed.append((best_time, param, res))
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

    repeat = '{:^3}'.format(rep)
    number = '{:^9}'.format(num)
    test_name = '{:^20}'.format(test_name)
    count = '{:^3}'.format(len(timed))

    title = 'Test case({t}): repeat({r}) of number({n})\nAll {c} tests took about {total} to process'.format(
        t=test_name, r=repeat, n=number, total=diff, c=count
    )

    with open(logname, 'w') as log:

        log.write('{0}\n'.format(tool_name()))
        log.write(title + "\n")
        print(title)

        for bt, p, r in timed:
            test_log = '{bt} // f{p} = {r}'.format(bt='{:8.5f}'.format(bt), p=p, r=r)
            log.write(test_log + "\n")

# -------------------------------------------------------
#                   Test compilation
# -------------------------------------------------------

def tests():

    def mk_bunch(repeat, number, (module_name, test_classes)):
        return [(module_name, t, repeat, number) for t in test_classes]

    prefs = get_prefs()
    repeat_fast = prefs[0]
    repeat_mid  = prefs[1]
    repeat_slow = prefs[2]
    number_fast = prefs[3]
    number_mid  = prefs[4]
    number_slow = prefs[5]

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

        ('string', [
                'StringEquals', 
                'StringConcat', 
                'StringFind',
                'StringReplace'
            ]
        )
    ]
    mid = [

        ('factorial', [
                'FactorialByMathLib', 
                'FactorialByRec', 
                'FactorialByLoop'
            ]
        ),

        ('factorial', [
                'FactorialBigByMathLib', 
                'FactorialBigByRec', 
                'FactorialBigByLoop'
            ]
        ),

        ('gcd', [
                'GCDByFractionsLib', 
                'GCDByRec', 
                'GCDByLoop'
            ]
        )
    ]
    slow = [

        ('loop', [
                'LoopByXRange', 
                'LoopByRange', 
                'LoopByWhile'
            ]
        )
    ]

    tests = []
    for t in fast: tests += mk_bunch(repeat_fast, number_fast, t)
    for t in mid: tests += mk_bunch(repeat_mid, number_mid, t)
    for t in slow: tests += mk_bunch(repeat_slow, number_slow, t)
    return tests # tuples - (module name, test class, repeat times, runs per test)

# -------------------------------------------------------
#                     Test runner
# -------------------------------------------------------

def main():
    for t in tests(): log_benchmark(t)

if __name__ == '__main__':
    main()


