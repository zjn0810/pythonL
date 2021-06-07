#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 08:59:13 2021

@author: zhangjn
"""


def selectSort(items):
    for fillslot in range(len(items)-1, 0, -1):
        posepoint = 0
        for location in range(1, fillslot + 1):
            if items[location] > items[posepoint]:
                posepoint = location
        temp = items[fillslot]
        items[fillslot] = items[posepoint]
        items[posepoint] = temp
    return items   
items = [23,45,56,34,345,26,66,88,46]
print(selectSort(items))               