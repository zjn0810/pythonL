#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 00:12:17 2021

@author: zhangjn
"""
import numpy as np 
import pandas as pd

d = pd.Series(range(30))

a = np.arange(30).reshape(3, 2, 5)



mSeries = pd.Series([5, 8, 0, 9], {'a', 'b', 'c', 'd'})

mDframe = pd.DataFrame(np.arange(10).reshape(2,5))

dt = {'one': pd.Series([1,2,3], index=['a', 'b', 'c']),
      'two': pd.Series([9,8,7,6],index=['a', 'b', 'c', 'd'])}
Ftd = pd.DataFrame(dt)

#Ftd['one']['d'] = 4


dl = {'城市': ['北京','上海','广州','深圳','沈阳'],
      '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
      '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
      '定基': [121.4, 127.8, 120.0, 145.5, 101.6],}
m = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])

newc = m.columns.insert(4, ' 新增')

newd = m.reindex(columns = newc, fill_value =200)



