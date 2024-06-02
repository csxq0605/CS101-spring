# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:19:58 2024

@author: Lenovo
"""

s=input()
n=len(s)
dp=[[0]*n for i in range(n)]
for i in range(2,n+1):
    for j in range(n-i+1):
        k=j+i-1
        if s[j]==s[k]:
            dp[j][k]=dp[j+1][k-1]
        else:
            dp[j][k]=min(dp[j+1][k],dp[j][k-1],dp[j+1][k-1])+1
print(dp[0][n-1])