# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:03:42 2024

@author: Lenovo
"""

n=int(input())
res=[0,1,2]
while res[-1]<n:
    res.append(res[-1]+res[-2]+1)
print(len(res)-1 if res[-1]==n else len(res)-2)