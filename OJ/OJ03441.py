# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:28:24 2024

@author: Lenovo
"""

n=int(input())
a,b,c,d=[0]*n,[0]*n,[0]*n,[0]*n
for i in range(n):
    a[i],b[i],c[i],d[i]=map(int,input().split())
dic={}
for i in range(n):
    for j in range(n):
        dic[a[i]+b[j]]=dic.get(a[i]+b[j],0)+1
ans=0
for i in range(n):
    for j in range(n):
        ans+=dic.get(-c[i]-d[j],0)
print(ans)