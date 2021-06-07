#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 04:08:29 2021

@author: zhangjn
"""

# 冒泡排序:代码

# =============================================================================
# def bubbleSort(items):
#     for times in range(len(items)-1, 0, -1):
#         for i in range(times):
#             if items[i] > items[i+1]:
#                 temp = items[i+1] 
#                 items[i+1] = items[i]
#                 items[i] =temp
#     return items
# 
# items = [23,45,56,34,345,26,66,88,46]
# print(bubbleSort(items))
# =============================================================================
                
# 冒泡排序:代码  性能改进
def bubbleSort(items):
    exchanges = True
    times = len(items) - 1
    while times > 0 and exchanges:
        exchanges = False
        print(times, end = ' ')
        for i in range(times):
            if items[i] > items[i + 1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp
                exchanges = True        
        times = times -1
    return items
        
items = [23,45,56,34,345,26,66,88,46]
print(bubbleSort(items))    
                
                
                
                
                