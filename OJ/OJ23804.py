# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:36:40 2024

@author: Lenovo
"""

n,m=map(int,input().split())
l=list(input().split())
for i in range(m):
    ans=0
    l1=list(input().split())
    for i in range(n):
        ans+=(l[i]==l1[i])
    print(ans)