#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:10:40 2021

@author: zhangjn
"""

import sys
sys.path.append('/home/zhangjn/software/pythonSpace/algorithm/')
from pythonds.basic.queue.myQueue import Queue

def hotPotato(namelist,num):
    simQueue = Queue()
    for name in namelist:
        simQueue.enqueue(name)
    simQueue.queue_print()
    while simQueue.size() > 1:
    #while len(simQueue) > 1:   X
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())
        simQueue.dequeue()
        simQueue.queue_print()
    return simQueue.dequeue()

print(hotPotato(['1','2','3','4','5','6'], 3))
print(hotPotato(['bill','david','susan','jane','keit','brad'], 7))