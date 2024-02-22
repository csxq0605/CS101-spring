# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 10:48:35 2024

@author: Lenovo
"""

def dfs(x,y):
    if matrix[x][y]==1:
        return True
    if x==0 or x==r-1 or y==0 or y==c-1:
        return False
    matrix[x][y]=1
    up=dfs(x-1,y)
    down=dfs(x+1,y)
    left=dfs(x,y-1)
    right=dfs(x,y+1)
    return up and down and left and right

matrix=[list(map(int,input().split(","))) for _ in range(10)]
ans=0
r,c=len(matrix),len(matrix[0])
for i in range(1,r-1):
    for j in range(1,c-1):
        if matrix[i][j]==0 and dfs(i,j):
            ans+=1
print(ans)