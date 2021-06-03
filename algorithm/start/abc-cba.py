#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:28:16 2021

@author: zhangjn
"""

# way 1 one by one  O(n^2)

# =============================================================================
# def reslove(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     else:
#         alist = list(s2)
#     for pose1 in range(len(s1)):
#         fond = False
#         for pose2 in range(len(alist)):
#             if s1[pose1] == alist[pose2]:
#                 fond = True
#                 break
#         if fond:
#             alist[pose2] = None
#             stillok = True
#         else:
#             stillok = False
#             return stillok
#     return stillok
# 
# if reslove('asd', 'avd'):
#     print('OK')
# else:
#     print('Not OK')
# =============================================================================
        
#way 2 sort    O(nlogn)

# =============================================================================
# def resolve(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     else:
#         alist1 = list(s1)
#         alist2 = list(s2)
#         alist1.sort()
#         alist2.sort()
#         for i in range(len(s1)):
#             if alist1[i] == alist2[i]:
#                 stillok = True
#             else:
#                 stillok = False
#                 break
#     return stillok 
# 
# if resolve('abc', 'cba'):
#     print('OK')
# else:
#     print('NOT OK')
# =============================================================================


def resove(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    
    for pose1 in range(len(s1)):
        pose1 = ord(s1[pose1]) - ord('a')
        c1[pose1] += 1
    for pose2 in range(len(s2)):
        pose2 = ord(s2[pose2]) - ord('a')
        c2[pose2] += 1
    for i in range(26):
        if c1[i] == c2[i]:
            stillok = True
        else:
            return False
    return stillok
            
if resove('hello', 'oleeh'):
     print('OK')
else:
    print('NOT OK')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
