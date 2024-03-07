# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:40:10 2023

@author: Lenovo
"""

def count(num):
    summ=0
    for i in range(n):
        summ+=l[i]//num
    return summ<k

n,k=map(int,input().split())
l=[0]*n
for i in range(n):
    l[i]=int(input())
left,right=1,sum(l)//k
while left<=right:
    mid=(left+right)//2
    if count(mid):
        right=mid-1
    else:
        left=mid+1
print(right)