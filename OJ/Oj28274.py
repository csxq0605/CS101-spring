# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:32:30 2024

@author: Lenovo
"""

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m or graph[x][y]==0:
        return
    graph[x][y]=0
    for i in range(4):
        dfs(x+move[i][0],y+move[i][1])

n,m=map(int,input().split())
move=[[-1,0],[1,0],[0,-1],[0,1]]
graph=[[int(i) for i in input()] for j in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ans+=1
            dfs(i,j)
print(ans)