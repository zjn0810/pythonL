#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 05:12:47 2021

@author: zhangjn
"""

def recursive_sum(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + recursive_sum(items[1:])
    
def recursive_mul(num):
    if num == 1:
        return 1
    else:
        return num * recursive_mul(num-1)
    
def exchangeBase(n, base):
    convertStr = '0123456789ABCDEF'
    if n < base:
        return convertStr[n]
    else:
        return exchangeBase(n//base,base) + convertStr[n % base]
    
def tellStory():
    print('从前有座山，山上有坐庙，庙里有个老和尚和一个小和尚，老和尚对小和尚说：')
    tellStory()

    
print(recursive_sum([1,2,2]))
print(recursive_mul(5))
print(exchangeBase(10, 2))
print(tellStory())


