#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:06:28 2021

@author: zhangjn
"""
'''
def rvs(s):
    if s == '':
        return s
    else :
        return rvs(s[1:]) + s[0]

print(rvs("asdfasdfasdf;jlkasdja;sdlfja"))
'''

# =============================================================================
# F(n) = 1        n = 1
# F(n) = 1        n = 2
# F(n) = F(n-1) + F(n-2)
# =============================================================================

# =============================================================================
# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     else :
#        return f(n-1) + f(n-2)
# 
# print(f(9))
# 
# =============================================================================

# =============================================================================
# 科赫曲线
# =============================================================================
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600,3)     # 0阶科赫曲线长度，阶数
    turtle.hideturtle()
main()
# =============================================================================
# import turtle
# def koch(size, n):
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#            turtle.left(angle)
#            koch(size/3, n-1)
# def main():
#     turtle.setup(600,600)
#     turtle.penup()
#     turtle.goto(-200, 100)
#     turtle.pendown()
#     turtle.pensize(2)
#     level = 1      # 3阶科赫雪花，阶数
#     koch(400,level)     
#     turtle.right(120)
#     koch(400,level)
#     turtle.right(120)
#     koch(400,level)
#     turtle.hideturtle()
# main()
# =============================================================================


















