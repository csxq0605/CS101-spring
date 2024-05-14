# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:00:11 2024

@author: Lenovo
"""

n=int(input())
h=[0]+[int(input()) for i in range(n)]
ans=0
for i in range(n,1,-1):
    for j in range(i-1,0,-1):
        if h[i]<=h[j]:break
        flag=True
        for k in range(j+1,i):
            if h[k]>=h[i] or h[k]<=h[j]:
                flag=False
                break
        if flag:
            ans=max(ans,i-j+1)
            if ans==n:
                break
if ans==1:
    ans=0
print(ans)