# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:13:40 2024

@author: Lenovo
"""

n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
if k==0:
    if l[0]>1:print(1)
    else:print(-1)
elif k<n and n>1 and l[k-1]==l[k]:
    print(-1)
else:
    print(l[k-1])