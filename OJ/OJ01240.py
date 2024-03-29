# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:03:48 2024

@author: Lenovo
"""

import sys
sys.setrecursionlimit(10**8)
def dfs(rs,rt,os,ot):
    if rs==rt:
        return 1
    son=0
    res=1
    l=rs+1
    r=os
    while l<=rt:
        while r<ot:
            if pre[l]==post[r]:
                son+=1
                break
            r+=1
        res*=dfs(l,l+r-os,os,r)
        l+=r-os+1
        rs=l-1
        os=r+1
    return res*C[m][son]

C=[[0]*30 for _ in range(30)]
for i in range(30):
    C[i][0]=1
for i in range(1,30):
    for j in range(1,i+1):
        C[i][j]=C[i-1][j-1]+C[i-1][j]
while True:
    m=input().split()
    if m[0]=="0":
        break
    m,pre,post=int(m[0]),m[1],m[2]
    n=len(pre)
    print(dfs(0,n-1,0,n-1))