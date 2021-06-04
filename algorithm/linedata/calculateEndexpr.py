#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 07:42:10 2021

@author: zhangjn
"""

import sys
sys.path.append('/home/zhangjn/software/pythonSpace/algorithm/')
from pythonds.basic.stack.myStack import Stack


def calculateEndopr(str_opera):
    operand = Stack()
    operalist = str_opera.split()
    for token in operalist:
        if token in '0123456789':
            operand.push(int(token))
        else:
            op2 = operand.pop()
            op1 = operand.pop()
            result = doMath(token, op1, op2)
            operand.push(result)
    return operand.pop()

def doMath(token, op1, op2):
    if token == '*':
        return op1 * op2
    elif token == '/':
        return op1 / op2
    elif token == '+':
        return op1 + op2
    else:
        return op1 - op2
        
print(calculateEndopr('1 2 + 3 * 5 *'))
        
       
        
       