# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:49:48 2024

@author: Lenovo
"""

n,p=map(int,input().split())
l=[[0]*2 for _ in range(p)]
for i in range(p):
    l[i]=list(map(int,input().split()))
jg=-1
for i in range(n):
    a=[0]*(n+1)
    for j in range(p):
        x=(l[j][0]+n-i)%n
        y=(l[j][1]+n-i)%n
        if x>y:x,y=y,x
        a[x]+=1
        a[y]-=1
    t=0
    js=0
    for k in range(n):
        t+=a[k]
        if t>0:
            js+=1
    if jg==-1 or jg>js:
        jg=js
print(jg)