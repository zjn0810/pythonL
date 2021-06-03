#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:16:15 2021

@author: zhangjn
"""

import turtle
q = turtle.Pen()
turtle.bgcolor("black")
sides = 7
colors =["red","orange","yellow","green","cyan","blue","blue","purple"]
for x in range(360):
    q.pencolor(colors[x%sides])
    q.forward(x*3/sides+x)
    q.left(360/sides+1)
    q.width(x*sides/200)