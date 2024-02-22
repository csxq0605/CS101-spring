# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:49:56 2023

@author: Lenovo
"""

n=int(input())
num=list(map(int,input().split()))
m=int(input())
num.sort()
f=0 
for i in range(n):
    left=i+1
    right=n
    while left<right:
        mid=(left+right)//2
        if num[mid]+num[i]==m:
            f=1
            print(num[i],num[mid])
            break
        if num[i]+num[mid]<m:
            left=mid+1
        else:
            right=mid-1
    if f==1:
        break
if f==0:
    print("No")