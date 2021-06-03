#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 05:38:13 2021

@author: zhangjn
"""

# way 1  one by  one

def resolve(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        alist = list(s2)
        
        for i in range(len(s1)):
            fond = False
            for m in range(len(alist)):
               if s1[i] == alist[m]:
                   fond = True
                   break
            if fond:
                alist[m] = None
                stillok = True
            else:
                stillok = False
                return stillok
    return stillok         
                
if resolve('abc', 'aac'):
    print("OK!")                 
else:
    print('NOT OK')
           
#way 2 sort

# =============================================================================
# def resove(s1, s2):
#     alist = list(s1)
#     alist2 = list(s2)
#     alist.sort()
#     alist2.sort()
#     for i in range(len(alist)):
#         if alist[i] == alist2[i]:
#             stillok = True
#         else:
#             stillok = False
#             return stillok
#     return stillok
#     
# if resove('zccxvb', 'bvxccz'):
#     print('OK')
# else:
#     print('NOT OK')
# 
# =============================================================================

#way 3 count 

# =============================================================================
# def resolve(s1, s2):
#     c1 = [0] * 26
#     c2 = [0] * 26
#     
#     for i in range(len(s1)):
#         pose = ord(s1[i]) - ord('a')
#         c1[pose] += 1
#     for i in range(len(s2)):
#         pose = ord(s2[i]) - ord('a')
#         c2[pose] += 1
#     for i in range(26):
#         if c1[i] == c2[i]:
#             stillok = True
#         else:
#             stillok = False
#             return stillok
#     return stillok
#         
# 
# if resolve('aad', 'dsa'):
#     print('OK!')
# else:
#     print('NOT OK!')
# =============================================================================































         
                    