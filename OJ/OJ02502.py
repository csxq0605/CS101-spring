# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:02:01 2024

@author: Lenovo
"""

import sys
import math
class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
def f(a,b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

input = sys.stdin.read
l=list(map(int,input().split()))
graph=[[0]*205 for i in range(205)]
nodes=[Node(l[0],l[1]),Node(l[2],l[3])]
cnt=2
flag=0
for i in range(4,len(l),2):
    x,y=l[i],l[i+1]
    node=Node(x,y)
    if x==-1 and y==-1:
        flag=0
        continue
    if flag==0:
        flag=1
    else:    
        graph[cnt-1][cnt]=graph[cnt][cnt-1]=f(nodes[-1],node)/40000
    nodes.append(node)
    cnt+=1
for i in range(cnt):
    for j in range(i+1,cnt):
        if graph[i][j]==0:
            graph[i][j]=graph[j][i]=f(nodes[i],nodes[j])/10000
vis=set()
vis.add(0)
d=graph[0]
for i in range(1,cnt):
    tmp=float("inf")
    for j in range(cnt):
        if j not in vis and d[j]<tmp:
            ind=j
            tmp=d[j]
    vis.add(ind)
    for j in range(cnt):
        if j not in vis and d[ind]+graph[ind][j]<d[j]:
            d[j]=d[ind]+graph[ind][j]
ans=60*d[1]
print(round(ans))