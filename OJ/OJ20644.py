# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:15:03 2024

@author: Lenovo
"""

m,n=map(int,input().split())
matrix=[list(map(int,input())) for i in range(m)]
dp=[[0]*(n+1) for i in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if matrix[i-1][j-1]:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
ans=0
for row in dp:
    ans+=sum(row)
print(ans)