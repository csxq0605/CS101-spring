# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:44:24 2024

@author: Lenovo
"""

n,m=map(int,input().split())
l=list(map(int,input().split()))
summ=[0]*(n+1)
for i in range(n):
    summ[i+1]=summ[i]+l[i]
dp=[[float("inf")]*(m+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0]=summ[i]*i
for i in range(1,n+1):
    for j in range(1,min(m,i)+1):
        for k in range(j-1,i):
            dp[i][j]=min(dp[i][j],dp[k][j-1]+(summ[i]-summ[k])*(i-k))
print(dp[n][m])