#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 01:11:10 2021

@author: zhangjn
"""

# =============================================================================
#          stack            <----
# **********************    ---->
# 
# Last in First Out
# =============================================================================

import sys
sys.path.append('/home/zhangjn/pythonL/MOOC/algorithm/')

from pythonds.basic.stack.myStack import Stack

# =============================================================================
# s = Stack()
# print(s.isEmpty())
# 
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.peek())
# print(s.size())
# =============================================================================

# =============================================================================
# def parChecker(str):
#     s = Stack()
#     index = 0
#     balanced = True
#     while index < len(str)  and balanced:
#         
#         if str[index] == '(':
#             s.push(str[index])
#         elif str[index] == ')':
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 s.pop()
#         index += 1
#     if s.isEmpty() and balanced:
#         return True
#     else:
#         return False           
#             
#     
# print(parChecker('((()((())))'))
# =============================================================================
    
def parChecker(str):
    s = Stack()
    index = 0
    balanced = True
    while index < len(str)  and balanced:      
        if str[index] in '([{':
            s.push(str[index])
        elif str[index] in ')]}':
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not maches(top, str[index]):
                    balanced = False
        index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False 

def maches(top,close):
    st1 = '([{'
    st2 = ')]}'
    return st1.index(top) == st2.index(close)
            
    
print(parChecker('(({}[]{(((((((((((([))))))))))))}))'))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
