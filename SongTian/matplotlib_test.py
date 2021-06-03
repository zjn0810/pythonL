#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:57:27 2021

@author: zhangjn
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

'''
plt.plot([3, 1, 4, 5, 1])
plt.ylabel('grade')
plt.show()
'''
'''
plt.plot([0, 2, 4, 6, 8],[3, 1, 4, 5, 2])
plt.ylabel('Grade')
plt.xlabel('Time')
plt.axis([-1,10,0,6])
plt.show()
'''
#plt.subplot(3,2,4)
'''
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0, 5.0, 0.02)
plt.subplot(211)
plt.plot(a, f(a))

plt.subplot(2, 1, 2)
plt.plot(a, np.cos(2*np.pi*a), 'r--')
plt.show()
'''
matplotlib.rcParams['font.family'] = 'SimHei'
a = np.arange(10)
plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
plt.ylabel('吕姗晓')
plt.show()













