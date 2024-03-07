# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:22:35 2023

@author: Lenovo
"""

t,m=map(int,input().split())
l=[[0]]
for i in range(m):
    l.append(list(map(int,input().split())))
ans=[0]*(t+1)
for i in range(1,m+1):
    for j in range(t,l[i][0]-1,-1):
        ans[j]=max(ans[j],ans[j-l[i][0]]+l[i][1])
print(ans[t])