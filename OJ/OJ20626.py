# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:55:30 2024

@author: Lenovo
"""

v=list(map(int,input().split()))
l=[0]*(len(v)+1)
for i in range(len(v)):
    l[i+1]=l[i]^v[i]
for i in range(10000):
    L,r=map(int,input().split())
    print(l[L]^l[r+1])