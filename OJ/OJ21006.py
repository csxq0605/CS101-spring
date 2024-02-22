# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:48:32 2024

@author: Lenovo
"""

def divide(x,y):
    dp=[[0]*(y+1) for i in range(x+1)]
    for i in range(1,y+1):
        dp[0][i]=1
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i<j:
                dp[i][j]=dp[i][i]
            else:
                dp[i][j]=dp[i][j-1]+dp[i-j][j]
    return dp[x][y]

n,k=map(int,input().split())
print(divide(n,k) if n>=k else divide(n,n))