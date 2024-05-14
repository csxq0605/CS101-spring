# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:09:48 2024

@author: Lenovo
"""

import heapq
x,y=map(int,input().split())
d=[(-1,0),(1,0),(0,1),(0,-1)]
matrix=[["1"]*(y+2)]+[["1"]+list(input())+["1"] for i in range(x)]+[["1"]*(y+2)]
for i in range(1,x+1):
    for j in range(1,y+1):
        if matrix[i][j]=="R":
            sx,sy=i,j
        elif matrix[i][j]=="C":
            ex,ey=i,j
        elif matrix[i][j]=="Y":
            kx,ky=i,j
heap=[]
heapq.heappush(heap,(0,sx,sy,0,[(sx,sy)]))
vis=set()
vis.add((sx,sy,0))
while heap:
    step,x,y,flag,path=heapq.heappop(heap)
    if x==ex and y==ey and flag:
        break
    elif x==kx and y==ky:
        flag=1
    for i in range(4):
        dx,dy=x+d[i][0],y+d[i][1]
        if matrix[dx][dy]!="1" and (dx,dy,flag) not in vis:
            vis.add((dx,dy,flag))
            heapq.heappush(heap,(step+1,dx,dy,flag,path+[(dx,dy)]))
for spot in path:
    print(*spot)