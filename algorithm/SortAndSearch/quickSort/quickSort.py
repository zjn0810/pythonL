#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 09:39:17 2021

@author: zhangjn
"""
def partion(alist,first,last):
    pivotvalue = alist[first]
    
    leftmark = first + 1
    rightmark = last
    
    done = False
    while not done:
        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
              leftmark = leftmark + 1
    
        while alist[rightmark] >= pivotvalue and \
            rightmark >= leftmark:
                rightmark = rightmark - 1
                
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
        
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    
    
    return rightmark


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partion(alist,first,last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
    
    
