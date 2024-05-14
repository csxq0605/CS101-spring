# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:47:39 2024

@author: Lenovo
"""

import sys
input=sys.stdin.read
data=input().split()
ind=0
n=int(data[ind])
ind+=1
m=int(data[ind])
ind+=1
vis=[0.5]*m
l=list(map(int,data[ind:ind+n]))
ans=[]
for num in l:
    ind=num%m
    while True:
        if vis[ind]==0.5 or vis[ind]==num:
            vis[ind]=num
            ans.append(ind)
            break
        ind=(ind+1)%m
print(*ans)