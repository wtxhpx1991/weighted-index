import functools
from operator import itemgetter
import numpy as np
import pandas as pd


def addabs(x, y, f):
    return f(x)+f(y)


addabs(-4, -5, abs)


def f(x):
    return x*x


r = map(f, range(10))
list(r)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
sorted(L, key=itemgetter(0))
sorted(L, key=lambda t: t[0])


def lazysum(*args):
    def getsum():
        ax = 0
        for i in args:
            ax = ax+i
        return ax
    return getsum


f = lazysum(1, 2, 3, 4, 5)
f


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
f1()
f2()
f3()


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s:' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print('2018-02-03')
now()
now.__name__


