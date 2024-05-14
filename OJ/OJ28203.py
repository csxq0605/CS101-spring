# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:38:40 2024

@author: Lenovo
"""

n=int(input())
a=list(map(int,input().split()))
stack=[]
f=[0]*n
for i in range(n):
    while stack and a[stack[-1]]<a[i]:
        f[stack.pop()]=i+1
    stack.append(i)
print(*f)