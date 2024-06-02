# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:20:50 2024

@author: Lenovo
"""

n=int(input())
r1=list(map(int,input().split()))
r2=list(map(int,input().split()))
l=[(r1[i]-r2[i],i) for i in range(n)]
l.sort(reverse=True)
ans=0
k=int(input())
for i in range(k):
    num,ind=l[i]
    ans+=r1[ind]
for i in range(k,n):
    num,ind=l[i]
    ans+=r2[ind]
print(ans)