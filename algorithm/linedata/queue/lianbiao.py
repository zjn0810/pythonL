#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 00:55:50 2021

@author: zhangjn
"""

import sys
sys.path.append('/home/zhangjn/software/pythonSpace/algorithm/')
from pythonds.basic.unorderedList.myunorderedlist import UnorderedList


m_list = UnorderedList()
showlist = []

for i in range(100):
    m_list.add(i)
    
for i in range(100):
    showlist.append(i)
    
m_list.add(999)