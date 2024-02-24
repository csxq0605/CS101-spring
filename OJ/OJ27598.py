# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:05:38 2024

@author: Lenovo
"""

n=int(input())
m=int(input())
l=[0]+list(map(int,input().split()))
dp=[[-float("inf")]*(n+1) for _ in range(m+1)]
dp[0][0]=0
for i in range(1,m+1):
    for j in range(1,n+1):
        for q in range(1,j+1):
            for k in range(1,min(j//q+1,i+1)):
                dp[i][j]=max(dp[i][j],dp[i-k][j-q*k]+k*l[q])
print(dp[m][n])