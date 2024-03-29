# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:33:18 2024

@author: Lenovo
"""

n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
dp=[0]*(m+1)
for i in range(n):
    for j in range(m,l[i][0]-1,-1):
        dp[j]=max(dp[j],dp[j-l[i][0]]+l[i][1])
print(max(dp))