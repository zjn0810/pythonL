#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:48:01 2021

@author: zhangjn
"""

def shellSort(items):
    sublistcount = len(items) // 2
    
    while sublistcount > 0:
        
        for startposition in range(sublistcount):
            gapInsertionSort(items,startposition,sublistcount)
            
        print("After increments of size",sublistcount,
                  "the list is",items)
        
        sublistcount = sublistcount // 2
    return items
        
def gapInsertionSort(items, start, gap):
    for i in range(start+gap,len(items),gap):
        
        currentvalue = items[i]
        position = i
        
        while position >= gap and \
            items[position-gap] > currentvalue:
                items[position] = items[position-gap]
                position = position - gap
        items[position] = currentvalue

    
items = [23,45,56,34,345,26,66,88,46]
print(items)
print(shellSort(items))
    
    
    
    
    
    
    
    
    
    
    