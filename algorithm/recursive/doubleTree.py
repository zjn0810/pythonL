#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 06:21:16 2021

@author: zhangjn
"""

import turtle

# =============================================================================
#t = turtle.Turtle()
#for i in range(4):
#     t.forward(100)
#     t.right(90)
# =============================================================================

# =============================================================================
# def drawLine(t, width):
#     if width > 0:
#         t.forward(width)
#         t.right(90)
#         drawLine(t, width-5)
# t = turtle.Turtle()
# drawLine(t, 100)
# turtle.done()
# =============================================================================

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len -15)
        t.right(20)
        t.backward(branch_len)
         
        
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(200)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(100)
t.hideturtle()
turtle.done()