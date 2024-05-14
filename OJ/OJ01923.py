# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:37:03 2024

@author: Lenovo
"""

def dfs(n,m):
    if m<0 or n*(n+1)<(m<<1):
        return 0
    elif m==0:
        return 1
    elif dp[n][m]!=-1:
        return dp[n][m]
    for i in range(1,n+1):
        dp[n][m]=dfs(n-i,m-i*(n-i))
        if dp[n][m]:
            return 1
    return 0
        
case=1
while True:
    n,m=map(int,input().split())
    if m==0 and n==0:
        break
    dp=[[-1]*(m+1) for i in range(n+1)]
    if dfs(n,m):
        print(f"Case {case}: {n} lines with exactly {m} crossings can cut the plane into {n+m+1} pieces at most.")
    else:
        print(f"Case {case}: {n} lines cannot make exactly {m} crossings.")
    case+=1