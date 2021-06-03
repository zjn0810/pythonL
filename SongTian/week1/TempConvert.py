# -*- coding: utf-8 -*-

TempStr = input('please input temprature:')

if  TempStr[-1] in ['F', 'f']:
    c = (eval(TempStr[0: -1]) - 32) / 1.8
    print("ConverTemp = {:.2f}C".format(c))
        
elif TempStr[-1] in ['C', 'c']:
    c = eval(TempStr[0: -1]) * 1.8 + 32
    print("ConverTemp = {:.2f}F".format(c))
    
else:
    print('input error!')