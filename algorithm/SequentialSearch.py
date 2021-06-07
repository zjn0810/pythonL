#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:52:51 2021

@author: zhangjn
"""
#顺序查找:无序表查找
# =============================================================================
# def SequentialSearch(items, element):
#     found = False
#     pos = 0
#     while pos < len(items) and not found:
#         if items[pos] == element:
#             found = True
#         else:
#             pos = pos + 1
#     return found
# =============================================================================

#顺序查找:有序表查找
# =============================================================================
# def SequentialSearch(items, element):
#     found = False
#     stop = False
#     pos = 0
#     while pos < len(items) and not found and not stop:
#         if items[pos] == element:
#             found = True
#         else:
#             if items[pos] > element:
#                 stop = True
#         pos = pos + 1
#     return found
# 
# print(SequentialSearch([1,23,34,45,70], 9))
# print(SequentialSearch([1,23,34,45,70], 70))
# =============================================================================

#二分查找

# =============================================================================
# def binarySearch(items, element):
#     found = False
#     first = 0
#     last = len(items)-1
#     
#     while last >= first and not found:
#         midpoint = (last + first) // 2
#         if items[midpoint] == element:
#             found = True
#         else:
#             if items[midpoint] > element:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found
# 
# print(binarySearch([1,23,34,45,70], 88))       
# =============================================================================


# 二分查找  递归算法

def binarySearch(items, element):
    if len(items) == 0:
        return False
    else:
        midpoint = len(items) // 2
        if items[midpoint] == element:
            return True
        else:
            if items[midpoint] > element:
                return binarySearch(items[:midpoint], element)
            else:
                return binarySearch(items[midpoint+1:], element)

print(binarySearch([1,23,34,45,70,80], 1))   










