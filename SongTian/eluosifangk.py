#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:36:04 2021

@author: zhangjn
"""

#_*_ coding:utf-8 _*_
from tkinter import *
import random
import time
import tkinter.messagebox


#俄罗斯方块界面的高度
HEIGHT  = 20

#俄罗斯方块界面的宽度
WIDTH   = 10

ACTIVE  = 1
PASSIVE = 0
TRUE    = 1
FALSE   = 0

style = [
            [[(0,0),(0,1),(1,1),(2,1)],[(1,0),(1,1),(1,2),(0,2)],[(0,1),(1,1),(2,1),(2,2)],[(1,0),(2,0),(1,1),(1,2)]],#j
            [[(1,0),(1,1),(1,2),(2,1)],[(1,0),(0,1),(1,1),(2,1)],[(1,0),(1,1),(1,2),(0,1)],[(0,1),(1,1),(2,1),(1,2)]],#T
            [[(0,1),(1,1),(2,1),(2,0)],[(0,0),(1,0),(1,1),(1,2)],[(0,1),(1,1),(2,1),(0,2)],[(1,0),(1,1),(1,2),(2,2)]],#反L
            [[(0,0),(0,1),(1,1),(1,2)],[(2,1),(1,1),(1,2),(0,2)],[(0,0),(0,1),(1,1),(1,2)],[(2,1),(1,1),(1,2),(0,2)]],#Z
            [[(1,0),(1,1),(0,1),(0,2)],[(0,1),(1,1),(1,2),(2,2)],[(1,0),(1,1),(0,1),(0,2)],[(0,1),(1,1),(1,2),(2,2)]],#反Z
            [[(0,0),(0,1),(1,1),(1,0)],[(0,0),(0,1),(1,1),(1,0)],[(0,0),(0,1),(1,1),(1,0)],[(0,0),(0,1),(1,1),(1,0)]],#田
            [[(1,0),(1,1),(1,2),(1,3)],[(0,1),(1,1),(2,1),(3,1)],[(1,0),(1,1),(1,2),(1,3)],[(0,1),(1,1),(2,1),(3,1)]]#长条
    ]

root=Tk();
root.title('俄罗斯方块')

class App(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        master.bind('<Up>',self.Up)
        master.bind('<Left>',self.Left)
        master.bind('<Right>',self.Right)
        master.bind('<Down>',self.Down)

        master.bind('<space>',self.Space)
        master.bind('<Control-Shift-Key-F12>',self.Play)
        master.bind('<Key-P>',self.Pause)
        master.bind('<Key-S>',self.StartByS)

        # rgb颜色值
        self.backg="#%02x%02x%02x" % (120,150,30)    #大背景
        self.frontg="#%02x%02x%02x" % (40,120,150)    #下一个形状颜色
        self.nextg="#%02x%02x%02x" % (150,100,100)    #小背景
        self.flashg="#%02x%02x%02x" % (210,130,100)    #炸的颜色

        self.LineDisplay=Label(master,text='Lines: ',bg='black',fg='red')
        self.Line=Label(master,text='0',bg='black',fg='red')
        self.ScoreDisplay=Label(master,text='Score: ',bg='black',fg='red')
        self.Score=Label(master,text='0',bg='black',fg='red')
        self.SpendTimeDisplay=Label(master,text='Time: ',bg='black',fg='red')
        self.SpendTime=Label(master,text='0.0',bg='black',fg='red')

        self.LineDisplay.grid(row=HEIGHT-2,column=WIDTH,columnspan=2)
        self.Line.grid(row=HEIGHT-2,column=WIDTH+2,columnspan=3)
        self.ScoreDisplay.grid(row=HEIGHT-1,column=WIDTH,columnspan=2)
        self.Score.grid(row=HEIGHT-1,column=WIDTH+2,columnspan=3)
        self.SpendTimeDisplay.grid(row=HEIGHT-4,column=WIDTH,columnspan=2)
        self.SpendTime.grid(row=HEIGHT-4,column=WIDTH+2,columnspan=3)

        self.TotalTime=0.0
        self.TotalLine=0
        self.TotalScore=0

        #游戏结束
        self.isgameover=FALSE
        #暂停
        self.isPause=FALSE
        #开始
        self.isStart=FALSE
        self.NextList=[]        #整个小背景
        self.NextRowList=[]     #一行小背景

        self.px=0
        self.py=0       #记录方块参考点

        #渲染小背景
        r=0;c=0
        for k in range(4*4):
            LN=Label(master,text='    ',bg=str(self.nextg),fg='white',relief=FLAT,bd=3)
            LN.grid(row=r,column=WIDTH+c,sticky=N+E+S+W)
            self.NextRowList.append(LN)
            c=c+1
            if c>=4:
                r=r+1;c=0
                self.NextList.append(self.NextRowList)
                self.NextRowList=[]

        #渲染大背景
        self.BlockList=[]
        self.BlockRowList=[]
        self.LabelList=[]
        self.LabelRowList=[]
        row=0;col=0
        for i in range(HEIGHT*WIDTH):
            L=Label(master,text='    ',bg=str(self.backg),fg='white',relief=FLAT,bd=4)
            L.grid(row=row,column=col,sticky=N+E+S+W)
            L.row=row;L.col=col;L.isactive=PASSIVE
            self.BlockRowList.append(0);    #大背景每个格子初始化为0值
            self.LabelRowList.append(L)
            col=col+1
            if col>=WIDTH:
                row=row+1;col=0
                self.BlockList.append(self.BlockRowList)
                self.LabelList.append(self.LabelRowList)
                self.BlockRowList=[]
                self.LabelRowList=[]

        #file
        fw=open('text.txt','a')
        fw.close()
        hasHead=FALSE
        f=open('text.txt','r')
        if f.read(5)=='score':
            hasHead=TRUE
        f.close()
        self.file=open('text.txt','a')
        if hasHead==FALSE:
            self.file.write('score    line    time    scorePtime    linePtime    scorePline    date/n')
            self.file.flush()

        self.time=1000
        self.OnTimer()

    def __del__(self):
        #self.file.close()
        pass

    def Pause(self,event):
        self.isPause=1-self.isPause

    def Up(self,event):
        BL=self.BlockList   #格子的值
        LL=self.LabelList   #格子Label

        Moveable=TRUE       #是否可旋转

        #代码编写开始
        nowStyle = style[self.xnow][(self.ynow)]
        newStyle = style[self.xnow][(self.ynow+1)%4]  #算出下一俄罗斯方块
        self.ynow = (self.ynow+1)%4 #此行代码非常重要，否则响应UP时，只能变第一次

        print("nowStyle:"+str(nowStyle)+"=====>>newStyle:"+str(newStyle))

        #根据现有形状中每个label的坐标计算出旋转后目标坐标(x,y)
        SourceList=[];DestList=[]

        for i in range(4):
            SourceList.append([ nowStyle[i][0]+self.px, nowStyle[i][1]+self.py])
            x = newStyle[i][0]+self.px
            y = newStyle[i][1]+self.py
            DestList.append([x, y])

            if x<0 or x>=HEIGHT or y<0 or y>=WIDTH : #or BL[x][y]==1 or LL[x][y].isactive==PASSIVE
                Moveable=FALSE

        if Moveable==TRUE:
            for i in range(len(SourceList)):
                self.Empty(SourceList[i][0],SourceList[i][1])
            for i in range(len(DestList)):
                self.Fill(DestList[i][0],DestList[i][1])

    def Left(self,event):
        BL=self.BlockList;LL=self.LabelList
        Moveable=TRUE
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if LL[i][j].isactive==ACTIVE and j-1<0:Moveable=FALSE
                if LL[i][j].isactive==ACTIVE and j-1>=0 and BL[i][j-1]==1 and LL[i][j-1].isactive==PASSIVE:Moveable=FALSE
        if Moveable==TRUE:
            self.py-=1
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    if j-1>=0 and LL[i][j].isactive==ACTIVE and BL[i][j-1]==0:
                        self.Fill(i,j-1);self.Empty(i,j)

    def Right(self,event):
        BL=self.BlockList;LL=self.LabelList
        Moveable=TRUE
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if LL[i][j].isactive==ACTIVE and j+1>=WIDTH:Moveable=FALSE
                if LL[i][j].isactive==ACTIVE and j+1<WIDTH and BL[i][j+1]==1 and LL[i][j+1].isactive==PASSIVE:Moveable=FALSE
        if Moveable==TRUE:
            self.py+=1
            for i in range(HEIGHT-1,-1,-1):
                for j in range(WIDTH-1,-1,-1):
                    if j+1<WIDTH and LL[i][j].isactive==ACTIVE and BL[i][j+1]==0:
                        self.Fill(i,j+1);self.Empty(i,j)

    def Down(self,event):
        BL=self.BlockList;LL=self.LabelList
        Moveable=TRUE
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if LL[i][j].isactive==ACTIVE and i+1>=HEIGHT:Moveable=FALSE
                if LL[i][j].isactive==ACTIVE and i+1<HEIGHT and BL[i+1][j]==1 and LL[i+1][j].isactive==PASSIVE:Moveable=FALSE
        if Moveable==TRUE and self.isStart :
            self.px+=1
            for i in range(HEIGHT-1,-1,-1):
                for j in range(WIDTH-1,-1,-1):
                    if i+1<HEIGHT and LL[i][j].isactive==ACTIVE and BL[i+1][j]==0:
                        self.Fill(i+1,j);self.Empty(i,j);
        if Moveable==FALSE:
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    LL[i][j].isactive=PASSIVE
            self.JudgeLineFill()
            self.Start()
            if self.isgameover==TRUE:showinfo('T_T','The game is over!');self.Distroy();return FALSE
            for i in range(4):
                for j in range(4):
                    self.NextEmpty(i,j)
            self.Rnd()
        return Moveable

    def Space(self,event):
        while 1:
            if self.Down(0)==FALSE:break

    def OnTimer(self):
        if self.isStart==TRUE and self.isPause==FALSE:
            self.TotalTime = self.TotalTime + float(self.time)/1000
            self.SpendTime.config(text=str(self.TotalTime))

        if self.isPause==FALSE:
            self.Down(0)
        if self.TotalScore>=1000:self.time=900
        if self.TotalScore>=2000:self.time=750
        if self.TotalScore>=3000:self.time=600
        if self.TotalScore>=4000:self.time=400
        self.after(self.time,self.OnTimer)      #随着分数增大，俄罗斯方块下降速度加快

    def JudgeLineFill(self):
        BL=self.BlockList;LL=self.LabelList
        count=0;LineList=[]
        for i in range(WIDTH):LineList.append(1)
        #display flash
        for i in range(HEIGHT):
            if BL[i]==LineList:
                count=count+1
                for k in range(WIDTH):
                    LL[i][k].config(bg=str(self.flashg))
                    LL[i][k].update()
        if count!=0:self.after(100)
        #delete block
        for i in range(HEIGHT):
            if BL[i]==LineList:
                #count=count+1
                for j in range(i,0,-1):
                    for k in range(WIDTH):
                        BL[j][k]=BL[j-1][k]
                        LL[j][k]['relief']=LL[j-1][k].cget('relief')
                        LL[j][k]['bg']=LL[j-1][k].cget('bg')
                for l in range(WIDTH):
                    BL[0][l]=0
                    LL[0][l].config(relief=FLAT,bg=str(self.backg))
        self.TotalLine=self.TotalLine+count
        if count==1:self.TotalScore=self.TotalScore+1*WIDTH
        if count==2:self.TotalScore=self.TotalScore+3*WIDTH
        if count==3:self.TotalScore=self.TotalScore+6*WIDTH
        if count==4:self.TotalScore=self.TotalScore+10*WIDTH
        self.Line.config(text=str(self.TotalLine))
        self.Score.config(text=str(self.TotalScore))

    def Fill(self,i,j):
        if j<0:return
        if self.BlockList[i][j]==1:self.isgameover=TRUE
        self.BlockList[i][j]=1
        self.LabelList[i][j].isactive=ACTIVE
        self.LabelList[i][j].config(relief=RAISED,bg=str(self.frontg))

    def Empty(self,i,j):
        self.BlockList[i][j]=0
        self.LabelList[i][j].isactive=PASSIVE
        self.LabelList[i][j].config(relief=FLAT,bg=str(self.backg))

    def Play(self,event):
        showinfo('Made in China','^_^')

    def NextFill(self,i,j):
        self.NextList[i][j].config(relief=RAISED,bg=str(self.frontg))

    def NextEmpty(self,i,j):
        self.NextList[i][j].config(relief=FLAT,bg=str(self.nextg))

    def Distroy(self):
        #save
        if self.TotalScore!=0:
            #cehkongfu
            savestr='%-9u%-8u%-8.2f%-14.2f%-13.2f%-14.2f%s/n' % (
                self.TotalScore,self.TotalLine,self.TotalTime
               ,self.TotalScore/self.TotalTime
               ,self.TotalLine/self.TotalTime
               ,float(self.TotalScore)/self.TotalLine
               ,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
            self.file.seek(0,2)
            self.file.write(savestr)
            self.file.flush()

        for i in range(HEIGHT):
            for j in range(WIDTH):
                self.Empty(i,j)
        self.TotalLine=0;self.TotalScore=0;self.TotalTime=0.0
        self.Line.config(text=str(self.TotalLine))
        self.Score.config(text=str(self.TotalScore))
        self.SpendTime.config(text=str(self.TotalTime))
        self.isgameover=FALSE
        self.isStart=FALSE
        self.time=1000
        for i in range(4):
            for j in range(4):
                self.NextEmpty(i,j)

    #游戏开始方块
    def Start(self):
        nextStyle = style[self.x][self.y]   #下一形状
        self.xnow = self.x
        self.ynow = self.y          #记录大背景中的方块
        self.py = random.randint(0,6)
        print("给py赋任意值:"+str(self.py))
        self.px = 0
        for ii in range(4):
            self.Fill(int(nextStyle[ii][0]),int(nextStyle[ii][1])+self.py)
        self.isStart=TRUE   #游戏开始

    #预处理方块
    def Rnd(self):
        self.x=random.randint(0,6)
        self.y=random.randint(0,3)
        nextStyle = style[self.x][self.y]   #下一形状
        for ii in range(4):
            self.NextFill(int(nextStyle[ii][0]),int(nextStyle[ii][1]))

    #游戏开始给出一次任意形状的方块
    def RndFirst(self):
        self.x=random.randint(0,6)  #选择第一个方块style
        self.y=random.randint(0,3)

    def Show(self):
        self.file.seek(0)
        strHeadLine=self.file.readline()
        dictLine={}
        strTotalLine=''
        for OneLine in self.file.readlines():
            temp=int(OneLine[:5])
            dictLine[temp]=OneLine

        list=sorted(dictLine.items(),key=lambda d:d[0])
        ii=0
        for onerecord in reversed(list):
            ii=ii+1
            if ii<11:
                strTotalLine+=onerecord[1]
        showinfo('Ranking', strHeadLine+strTotalLine)

    def StartByS(self,event):
        self.RndFirst()
        self.Start()
        self.Rnd()

def Start():
    app.RndFirst()
    app.Start()
    app.Rnd()

def End():
    app.Distroy()

def Set():
    print("设置功能待完善...")

def Show():
    app.Show()

#主菜单
mainmenu=Menu(root)
root['menu']=mainmenu

#二级菜单：game
gamemenu=Menu(mainmenu)
mainmenu.add_cascade(label='游戏',menu=gamemenu)
gamemenu.add_command(label='开始',command=Start)
gamemenu.add_command(label='结束',command=End)
gamemenu.add_separator()
gamemenu.add_command(label='退出',command=root.quit)

#二级菜单：set
setmenu=Menu(mainmenu)
mainmenu.add_cascade(label='设置',menu=setmenu)
setmenu.add_command(label='设置',command=Set)

#二级菜单：show
showmenu=Menu(mainmenu)
mainmenu.add_cascade(label='展示',menu=showmenu)
showmenu.add_command(label='展示',command=Show)

#绑定功能

app=App(root)
#程序入口
root.mainloop()