#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 01:46:45 2021

@author: zhangjn
"""

# =============================================================================
# 归并排序Merge Sort
# ❖ 下面我们来看看分治策略在排序中的应用
# ❖ 归并排序是递归算法,思路是将数据表持
# 续分裂为两半,对两半分别进行归并排序
#    递归的基本结束条件是:数据表仅有1个数据项
# ,自然是排好序的;
#    缩小规模:将数据表分裂为相等的两半,规模减
# 为原来的二分之一;
#    调用自身:将两半分别调用自身排序,然后将分
# 别排好序的两半进行归并,得到排好序的数据表
# =============================================================================

# =============================================================================
# def mergeSort(items):
# #    print(items)
#     if len(items) > 1:
#         mid = len(items) // 2
#         lefthalf = items[:mid]
#         righthalf = items[mid:]
#         
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#         
#         i= j= k= 0
#         while i<len(lefthalf) and j<len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 items[k] = lefthalf[i]
#                 i = i + 1
#             else:
#                 items[k] = righthalf[j]
#                 j = j + 1
#             k = k + 1
#             
#         while i < len(lefthalf):
#             items[k] = lefthalf[i]
#             i = i + 1
#             k = k + 1
#         
#         while j < len(righthalf):
#             items[k] = righthalf[j]
#             j = j + 1
#             k = k + 1
#     return items
# 
# items = [23,45,56,34,345,26,66,88,46]
# print(mergeSort(items))
# =============================================================================


#pythonic

def merge_sort(items):
    print(items)
    if len(items)<=1:
        return items
    
    middle = len(items) // 2
    left =merge_sort(items[0:middle])
    right = merge_sort(items[middle:])
    
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
            
    merged.extend(right if right else left)
    print('merged',merged)
    return merged
items = [23,45,56,34,345,26,66,88,46]
print(merge_sort(items))

