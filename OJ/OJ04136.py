# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 10:16:21 2024

@author: Lenovo
"""

R=int(input())
a=[0]*R
n=int(input())
for i in range(n):
    L,T,W,H=map(int,input().split())
    for j in range(L,L+W):
        a[j]+=H
le,ri=0,R
while True:
    if le>=ri:
        break
    else:
        mi=(le+ri)//2
        x=sum(a[:mi])
        y=sum(a[mi:])
        if x>=y:
            ri=mi
        else:
            le=mi+1
while True:
    if le==R:
        print(le)
        break
    elif a[le]==0:
        le+=1
    else:
        print(le)
        break