# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:11:47 2023

@author: Lenovo
"""

def check(num):
    ans,tot=1,0
    for i in l:
        if tot+i<=num:
            tot+=i
        else:
            tot=i
            ans+=1
        if ans>m:
            return False
    return True

n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(int(input()))
left,right=max(l),n*max(l)//m
while right>=left:
    mid=(left+right)//2
    if check(mid):
        res=mid
        right=mid-1
    else:
        left=mid+1
print(res)