# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:34:24 2024

@author: Lenovo
"""

def dfs(i,j):
    if dp[i][j]>0:
        return dp[i][j]
    else:
        for k in range(4):
            if 0<=i+d[k][0]<r and 0<=j+d[k][1]<c and maze[i][j]>maze[i+d[k][0]][j+d[k][1]]:
                dp[i][j]=max(dp[i][j],dfs(i+d[k][0],j+d[k][1])+1)
    return dp[i][j]

r,c=map(int,input().split())
maze=[]
for i in range(r):
    l=list(map(int,input().split()))
    maze.append(l)
dp=[[0]*c for _ in range(r)]
d=[[-1,0],[1,0],[0,1],[0,-1]]
ans=0
for i in range(r):
    for j in range(c):
        ans=max(ans,dfs(i,j))
print(ans+1)