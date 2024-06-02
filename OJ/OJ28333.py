# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:33:53 2024

@author: Lenovo
"""

n,k=map(int,input().split())
l=[1]+list(map(int,input().split()))
for i in range(1,n+1):
    l[i]*=l[i-1]
ans=0
for i in range(n):
    for j in range(i+1,n+1):
        if l[j]//l[i]>=k:
            ans=(ans+n-j+1)%233333
            break
print(ans)