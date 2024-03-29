# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:27:09 2024

@author: Lenovo
"""

n=int(input())
f=[0]*(n+1)
f[0]=f[1]=1
for i in range(2,n+1):
    for j in range(i):
        f[i]+=f[j]*f[i-j-1]
print(f[n])