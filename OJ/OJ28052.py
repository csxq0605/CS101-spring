# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:51:47 2024

@author: Lenovo
"""

from heapq import heappush,heappop
def bfs(color):
    move=[(0,-1),(1,0),(1,1),(0,1),(-1,0)]
    heap=[]
    vis=set()
    if color==1:
        for i in range(n):
            if matrix[0][i]==0:
                heappush(heap,(1,0,i))
            elif matrix[0][i]==1:
                heappush(heap,(0,0,i))
            vis.add((0,i))
    else:
        for i in range(n):
            if matrix[i][0]==0:
                heappush(heap,(1,i,0))
            elif matrix[i][0]==2:
                heappush(heap,(0,i,0))
            vis.add((i,0))
    while heap:
        step,x,y=heappop(heap)
        if color==1 and x==n-1:
            return step
        elif color==2 and y==n-1:
            return step
        for i in range(color-1,color+3):
            dx,dy=x+move[i][0],y+move[i][1]
            if 0<=dx<n and 0<=dy<n and (dx,dy) not in vis:
                if matrix[dx][dy]==0:
                    heappush(heap,(step+1,dx,dy))
                elif matrix[dx][dy]==color:
                    heappush(heap,(step,dx,dy))
                vis.add((dx,dy))
    return -1

n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
count1=count2=0
for i in range(n):
    for j in range(n):
        count1+=int(matrix[i][j]==1)
        count2+=int(matrix[i][j]==2)
if count1<=count2:
    ans=bfs(1)
else:
    ans=bfs(2)
print(ans)