#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 01:15:14 2021

@author: zhangjn
"""

import time

'''
scale = 10
print("-------start to insall------------")
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    print('{:^3.0f}%[{}->{}]'.format(c,a,b))
    time.sleep(0.5)
print("-------install successfully-------")
'''

for i in range(101):
    print('\r{:3}%'.format(i),end="")
    time.sleep(0.1)