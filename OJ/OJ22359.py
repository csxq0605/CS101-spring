# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:21:46 2024

@author: Lenovo
"""

from math import sqrt
n=10000
ls,x,y=[True]*(n+1),2,int(sqrt(n))+1
while x<y:
    if ls[x]==True:
        for i in range(x*2,n+1,x):
            ls[i]=False
    x+=1
ls=set([i for i in range(2,n+1) if ls[i]==True])

n=int(input())
for i in ls:
    if (n-i) in ls:
        print(i,n-i)
        break