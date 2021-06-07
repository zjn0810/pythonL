#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:56:14 2021

@author: zhangjn
"""

# 插入排序:
    
def insertsort(items):
    for index in range(1, len(items)):
        current = items[index]
        position = index
        while position > 0 and items[position - 1] > current:
            items[position] = items[position -1]
            position = position -1
            
        items[position] = current
        
    return  items

items = [23,45,56,34,345,26,66,88,46]
print(insertsort(items))  