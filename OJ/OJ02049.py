# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:39:00 2024

@author: Lenovo
"""

from heapq import heappush,heappop
di=[(0,-1),(-1,0),(0,1),(1,0)]
N=201
while True:
    m,n=map(int,input().split())
    if m==-1 and n==-1:
        break
    maze=[[[0]*4 for i in range(N)] for _ in range(N)]
    vis=[[False]*(N) for i in range(N)]
    for _ in range(m):
        x,y,d,t=map(int,input().split())
        if d:
            for i in range(t):
                maze[x][y+i][1]=1
                maze[x-1][y+i][3]=1
        else:
            for i in range(t):
                maze[x+i][y][0]=1
                maze[x+i][y-1][2]=1
    for _ in range(n):
        x,y,d=map(int,input().split())
        if d:    
            maze[x][y][1]=2
            maze[x-1][y][3]=2
        else:
            maze[x][y][0]=2
            maze[x][y-1][2]=2
    x,y=map(float,input().split())
    x,y=int(x+1e-4),int(y+1e-4)
    if (n==0 and m==0) or (x<=0 or y<=0 or x>=199 or y>=199):
        print(0)
        continue
    heap=[]
    heappush(heap,(0,x,y))
    vis[x][y]=True
    res=float("inf")
    while heap:
        num,x,y=heappop(heap)
        if x==0 or y==0 or x>=199 or y>=199:
            res=num
            break
        for i in range(4):
            dx,dy=x+di[i][0],y+di[i][1]
            if not vis[dx][dy] and maze[x][y][i]!=1:
                heappush(heap,(num+int(maze[x][y][i]==2),dx,dy))
                vis[dx][dy]=True
    print(res if res!=float("inf") else -1)