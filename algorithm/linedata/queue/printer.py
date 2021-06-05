#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 08:32:55 2021

@author: zhangjn
"""

import sys
sys.path.append('/home/zhangjn/software/pythonSpace/algorithm')
from pythonds.basic.queue.myQueue import Queue

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining -1
            if self.timeRemaining <= 0:
                self.currentTask = None
            
    def isBusy(self):
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() \
                            * 60/self.pagerate
                    
class  Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages
    
    def waitTime(self, currentTask):
        return currentTask - self.timestamp
    
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    
    for currentSecond in range(numSeconds):
        
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.isBusy()) and \
                (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append( \
                nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
            
        labprinter.tick()


    averageWait = sum(waitingtimes) / len(waitingtimes)
    print('Average Wait %6.2f secs %3d tasks remaining.' \
      %(averageWait, printQueue.size()))
        
for i in range(10):
    simulation(3600, 10)



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        