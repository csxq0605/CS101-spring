# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:43:06 2024

@author: Lenovo
"""

import heapq
move=[(-1,0),(0,1),(1,0),(0,-1)]
while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    maze=[list(input()) for i in range(m)]
    for i in range(m):
        for j in range(n):
            if maze[i][j]=="Y":
                sx,sy=i,j
            elif maze[i][j]=="T":
                ex,ey=i,j
                maze[i][j]="E"
    heap=[]
    vis=set()
    flag=False
    heapq.heappush(heap,(0,sx,sy))
    vis.add((sx,sy))
    while heap:
        step,x,y=heapq.heappop(heap)
        if x==ex and y==ey:
            flag=True
            break
        for i in range(4):
            dx,dy=x+move[i][0],y+move[i][1]
            if 0<=dx<m and 0<=dy<n and (dx,dy) not in vis:
                vis.add((dx,dy))
                if maze[dx][dy]=="E":
                    heapq.heappush(heap,(step+1,dx,dy))
                elif maze[dx][dy]=="B":
                    heapq.heappush(heap,(step+2,dx,dy))
    print(step if flag else -1)