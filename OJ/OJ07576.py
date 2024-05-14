# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:22:01 2024

@author: Lenovo
"""

def build(l,n):
    if n==1:
        return l
    a,b=[],[]
    for i in range(0,n,2):
        a.append(max(l[i],l[i+1]))
        b.append(min(l[i],l[i+1]))
    return build(b,n//2)+a
    
n,m=map(int,input().split())
l=list(map(int,input().split()))
print(*build(l,n))
for i in range(m):
    ind,num=map(int,input().split())
    l[ind]=num
    print(*build(l,n))