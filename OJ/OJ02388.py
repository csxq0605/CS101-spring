# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:30:18 2024

@author: Lenovo
"""

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
print(l[n//2])