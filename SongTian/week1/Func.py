#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 02:43:06 2021

@author: zhangjn
"""

#n!//m
'''
def fact (n,m=1):
    s = 1
    for i in range(1, n+1):
        s = s*i
    return s//m

print(fact(5))
'''
'''
def fact (n, *b):
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s

print(fact(5,2,3))
'''
'''
def fact (n, *b):
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s, item

x,y = fact(5,2,3)

print(x,y)
print(fact(5,2,3))
'''
'''
#global bianliang

ls = ['I', 'A']
def func (a):
    #ls = []
    ls.append(a)
    return ls
func('C')
print(ls)

'''

#lambda
f = lambda x, y : x + y
f(10,15)










