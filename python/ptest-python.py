
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-09-04

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
    for param in params:
        sample = '%s(*%s)' % (test_func, param)
        best_time = min(benchmarker(sample, setup=setup, repeat=repeat, number=number))
        yield (test_name, best_time, number, param)

def log_benchmark(logname, bench_args):
    with open(logname, 'a') as log:
        timed = benchmark(*bench_args)
        for t, bt, n, p in timed:
            test_name = '{:^20}'.format(t)
            best_time = '  {:0.5f}s  '.format(bt)
            runs_count = '{:^15}'.format(n)
            parameter = '{:^15}'.format(p)
            to_log = '[%s] runs of [%s] took at best [%s] with parameter = [%s]\n' % (runs_count, test_name, best_time, parameter)
            log.write(to_log)
            # print(to_log)

def now():
    from time import strftime
    from datetime import datetime
    return datetime.now()

def logname(test_name): 
    folder = 'results'
    lang = PythonTest.subject()
    ext  = 'log'
    return '%s/%s-%s.%s' % (folder, test_name, lang, ext)

def tool_name():
    import sys
    return 'Python: %s' % sys.version

# -------------------------------------------------------
#                     Test runner
# -------------------------------------------------------

def tests():

    def create_bunch(repeat, number, (module_name, test_classes)):
        return [(t, module_name, repeat, number) for t in test_classes]

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

    default_repeat = 1
    number_for_fast = 1000000
    number_for_mid  = 10000
    number_for_slow = 100

    tests = []
    for t in fast: tests += create_bunch(default_repeat, number_for_fast, t)
    for t in mid: tests += create_bunch(default_repeat, number_for_mid, t)
    for t in slow: tests += create_bunch(default_repeat, number_for_slow, t)
    return tests # triples - (test class, repeat times, runs per repeat)

def main():
    tool = tool_name()
    for b in tests():
        log = logname(b[0])
        module_name = b[1]
        test_name = b[0]
        print('Test  : [%s] %s' % (module_name, eval(test_name + '.name()')))
        print('Start : %s' % now())
        with open(log, 'w+') as f: 
            f.write('%s\n' % tool)
            f.write('Start tests: %s\n' % now())
        log_benchmark(log, b)
        with open(log, 'a') as f: f.write('End tests:   %s\n' % now())
        print('End   : %s' % now())

if __name__ == '__main__':
    main()


