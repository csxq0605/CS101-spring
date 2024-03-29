# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:09:55 2024

@author: Lenovo
"""

while True:
    try:
        n=int(input())
        dp=[[0]*(n+1)for i in range(n+1)]
        for i in range(1,n+1):
            dp[i][1]=1
            dp[1][i]=1
        for i in range(1,n+1):
            for j in range(2,n+1):
                if j>i:
                    dp[i][j]=dp[i][i]
                elif j==i:
                    dp[i][j]=dp[i][j-1]+1
                else:
                    dp[i][j]=dp[i][j-1]+dp[i-j][j]
        print(dp[n][n])
    except EOFError:
        break