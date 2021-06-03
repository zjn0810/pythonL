#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:12:33 2021

@author: zhangjn
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'

plt.plot([3, 1, 4, 2, 5])

plt.ylabel('Price')
plt.title('title')
plt.text(1, 3, '--r')

plt.show()




