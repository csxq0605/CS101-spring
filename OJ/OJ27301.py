# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:57:29 2024

@author: Lenovo
"""

n,a,b=map(int,input().split())
line=list(map(int,input().split()))
l,r=0,n-1
t=n
ta,tb=a,b
ans=0
while t>1:
    if ta>=line[l]:
        ta-=line[l]
        l+=1
        t-=1
    else:
        ta=a
        ans+=1
        ta-=line[l]
        l+=1
        t-=1
    if tb>=line[r]:
        tb-=line[r]
        r-=1
        t-=1
    else:
        tb=b
        ans+=1
        tb-=line[r]
        r-=1
        t-=1
if t==1:
    if ta<line[l] and tb<line[r]:
        ans+=1
print(ans)