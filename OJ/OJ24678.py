# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:38:48 2024

@author: Lenovo
"""

w,n=map(int,input().split())
l=list(map(int,input().split()))
left,ans,tmp=0,float("inf"),0
for i in range(n):
    tmp+=l[i]
    while tmp>=w:
        ans=min(ans,i-left+1)
        tmp-=l[left]
        left+=1
print(ans if ans!=float("inf") else 0)