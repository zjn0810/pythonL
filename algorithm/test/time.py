#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:08:28 2021

@author: zhangjn
"""
from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]
    
def test4():
    l = list(range(1000))


t1 = Timer('test1()', 'from __main__ import test1')
print('concat %f seconds\n'%t1.timeit(number = 1000))

t2 = Timer('test2()', 'from __main__ import test2')
print('append %f seconds\n'%t2.timeit(number = 1000))

t3 = Timer('test3()', 'from __main__ import test3')
print('comprehension %f seconds\n'%t3.timeit(number = 1000))

t4 = Timer('test4()', 'from __main__ import test4')
print('list range %f seconds\n'%t4.timeit(number = 1000))


x = list(range(2000000))
t5 = Timer('x.pop(0)', 'from __main__ import x')
print('pop(0) %f seconds\n'%t4.timeit(number = 1000))
y = list(range(2000000))
t6 = Timer('y.pop()', 'from __main__ import y')
print('pop() %f seconds\n'%t4.timeit(number = 1000))









