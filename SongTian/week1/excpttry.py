#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 01:41:42 2021

@author: zhangjn
"""

try:
    num = eval(input("please input a Int number:"))
    print(num**2)
except NameError:
    print("your input is not a Int number!")