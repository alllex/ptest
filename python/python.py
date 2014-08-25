
# Project: ptest
# Module:  python
# Author:  alllex
# Date  :  2014-08-23


def benchmark(test, repeat=1, number=1):
    from timeit import repeat as benchmarker
    setup = 'from __main__ import %s' % test #'; '.join(setups)
    testf = test + '.test'
    params = eval(test + '.params()')
    for param in params:
        sample = '%s(%s)' % (testf, param)
        best_time = min(benchmarker(sample, setup=setup, repeat=repeat, number=number))
        yield (test, best_time, number, param)

class Test:
    @staticmethod
    def test(param): pass
    @staticmethod
    def params(): pass

class Loop(Test):

    @staticmethod
    def test(param):
        n = param
        sum = 0
        for i in xrange(1, n + 1):
            sum += i
            sum %= i
            sum ^= i
        # return sum

    @staticmethod
    def params():
        return (1 << x for x in range(10, 16, 2))

class GCD(Test):

    @staticmethod
    def test(param):
        from fractions import gcd
        # gcds = []
        pairs = param
        for a, b in pairs: 
            g = gcd(a, b)
            # gcds.append(g)
        # return gcds

    @staticmethod
    def params():
        from itertools import product
        sample = range((1 << 10) - 1, (1 << 12) - 1, 1 << 5)
        def shift(d): return map(lambda x: x + d, sample)
        for pd in xrange(5, 9 + 1, 2):
            d = 1 << pd
            yield [pair for pair in product(shift(-d), shift(+d))]

class Factorial(Test):

    @staticmethod
    def test(param):
        from math import factorial
        n = param
        f = factorial(n)
        # return sum

    @staticmethod
    def params():
        return xrange(2000, 10000 + 1, 2000)

def log_benchmark(logname, bench_args):
    with open(logname, 'a') as log:
        timed = benchmark(*bench_args)
        for t, bt, n, p in timed:
            test_name = '{:^15}'.format(t)
            best_time = '  {:0.5f}s  '.format(bt)
            runs_count = '{:^15}'.format(n)
            parameter = '{:^15}'.format(p)
            to_log = '[%s] runs of [%s] took at best [%s] with parameter = [%s]\n' % (runs_count, test_name, best_time, parameter)
            log.write(to_log)
            print(to_log)


def now():
    from time import strftime
    from datetime import datetime
    return datetime.now()

print(now())

def main():
    prog = 'ptest'
    lang = 'python'
    ext  = 'log'
    def logname(test): return '%s-%s-%s.%s' % (prog, lang, test, ext)
    tests = ['Loop', 'GCD', 'Factorial']
    # args_of_benches = [
    #         ('Loop', 100, 100),
    #         ('GCD',  100, 100),
    #         ('Factorial', 100, 100)
    #     ]
    args_of_benches = [(test, 100, 100) for test in tests]
    for b in args_of_benches:
        log = logname(b[0])
        print('Start tests: %s\n' % log)
        with open(log, 'w+') as f: f.write('Start tests: %s\n' % now())
        log_benchmark(log, b)
        with open(log, 'a') as f: f.write('End tests:   %s\n' % now())
        print('End test:    %s\n' % log)

# if __name__ == '__main__':
#     main()


