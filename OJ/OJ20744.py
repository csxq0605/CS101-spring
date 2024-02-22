# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:51:46 2024

@author: Lenovo
"""

l=list(map(int,input().split(",")))
l1=[0]*len(l)
for i in range(len(l)):
    l1[i]=max(l[i],l1[i-1]+l[i])
maxn=max(l1)
if maxn<0:
    print(max(l))
    quit()
left,right=[0]*(len(l)+1),[0]*(len(l)+1)
for i in range(len(l)):
    left[i]=max(0,left[i-1]+l[i])
    right[len(l)-i-1]=max(0,right[len(l)-i]+l[len(l)-i-1])
ans=maxn
for i in range(len(l)):
    ans=max(ans,left[i-1]+right[i+1])
print(ans)