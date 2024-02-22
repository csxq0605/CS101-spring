# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:15:51 2024

@author: Lenovo
"""

import heapq
d=[[1,0],[0,1],[-1,0],[0,-1]]
dic={"south":0,"east":1,"north":2,"west":3}
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    matrix=[list(map(int,input().split())) for _ in range(n)]
    maze=[[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                maze[i][j]=maze[i][j+1]=maze[i+1][j]=maze[i+1][j+1]=1
    b1,b2,e1,e2,direction=input().split()
    start=(0,int(b1),int(b2),dic[direction])
    end=(int(e1),int(e2))
    flag=False
    vis=[[[False]*4 for i in range(m+1)] for _ in range(n+1)]
    vis[int(b1)][int(b2)][dic[direction]]=True
    heap=[]
    heapq.heappush(heap,start)
    while heap:
        t,x0,y0,direction=heapq.heappop(heap)
        if (x0,y0)==end:
             flag=True
             break
        for i in range(1,4):
            dx0,dy0=x0+d[direction][0]*i,y0+d[direction][1]*i
            if not (0<dx0<n and 0<dy0<m and maze[dx0][dy0]!=1):
                break
            if not vis[dx0][dy0][direction]:
                heapq.heappush(heap,(t+1,dx0,dy0,direction))
                vis[dx0][dy0][direction]=True
        if not vis[x0][y0][(direction+1)%4]:
            heapq.heappush(heap,(t+1,x0,y0,(direction+1)%4))
            vis[x0][y0][(direction+1)%4]=True
        if not vis[x0][y0][(direction+3)%4]:
            heapq.heappush(heap,(t+1,x0,y0,(direction+3)%4))
            vis[x0][y0][(direction+3)%4]=True
    print(t if flag else -1)