# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 00:24:25 2024

@author: Lenovo
"""

n=int(input())
dp=[0]*(n+1)
dp[1]=dp[2]=1
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
print(dp[-1])