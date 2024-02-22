# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:47:58 2024

@author: Lenovo
"""

m,n=map(int,input().split())
matrix=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(m)]
dp=[[[0]*(m+1) for _ in range(m+1)] for i in range(n+m)]
for i in range(1,m+n):
    for j in range(1,m+1):
        if j>i:
            break
        for k in range(1,m+1):
            if k>i:
                break
            dp[i][j][k]=max(dp[i-1][j-1][k],dp[i-1][j-1][k-1],dp[i-1][j][k],dp[i-1][j][k-1])
            dp[i][j][k]+=matrix[j][i-j+1]+matrix[k][i-k+1]
            if j==k:
                dp[i][j][k]-=matrix[j][i-j+1]
print(dp[-1][-1][-1])