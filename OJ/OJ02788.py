# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:10:57 2024

@author: Lenovo
"""

while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    ans=num=1
    left,right=m*2,m*2+1
    while right<=n:
        num*=2
        ans+=num
        left*=2
        right=right*2+1
    if left<=n:
        ans+=n-left+1
    print(ans)