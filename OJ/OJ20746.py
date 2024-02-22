# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:09:31 2024

@author: Lenovo
"""

def check(x):
    ans=0
    for num in list:
        ans+=ceil(num/x)
    return ans>t

from math import ceil
list=list(map(int,input().split(",")))
t=int(input())
l,r=ceil(sum(list)/t),max(list)
while l<r:
    mid=(l+r)//2
    if check(mid):
        l=mid+1
    else:
        r=mid
print(r)