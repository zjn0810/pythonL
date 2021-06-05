#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:35:04 2021

@author: zhangjn
"""

# =============================================================================
# “回文词”判定
# ❖ “回文词”指正读和反读都一样的词
# 如radar、madam、toot
# 中文“上海自来水来自海上”
# “山东落花生花落东山”
# =============================================================================

import sys
sys.path.append('/home/zhangjn/software/pythonSpace/algorithm/')
from pythonds.basic.queue.myDeQueue import Dequeue

def checker(words):
    deq = Dequeue()
    
    for ch in words:
        deq.addRear(ch)
    
    stillOK = True
    while deq.size()>1 and stillOK:
        if deq.removeFront() != deq.removeRear():
            stillOK = False
    return stillOK

print(checker('上海自来水来自海上'))
            
            
            
            
            