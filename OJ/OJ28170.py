# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:57:46 2024

@author: Lenovo
"""

grid=[]
for _ in range(10):
    row=list(input().strip())
    grid.append(row)
visited=[[False]*10 for _ in range(10)]  
dir_x=[-1,0,1,0] 
dir_y=[0,-1,0,1]
pondCount = 0
for i in range(10):
    for j in range(10):
        if grid[i][j]=='.' and not visited[i][j]:
            pondCount+=1
            stack=[(i,j)]
            visited[i][j]=True
            while stack:
                x,y=stack.pop()
                for k in range(4):
                    nx,ny=x+dir_x[k],y+dir_y[k]
                    if nx>=0 and nx<10 and ny>=0 and ny<10 and grid[nx][ny]=='.' and not visited[nx][ny]:
                        stack.append((nx,ny))
                        visited[nx][ny]=True
print(pondCount)