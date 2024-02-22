# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:26:48 2024

@author: Lenovo
"""

n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]+1
print(dp[n])