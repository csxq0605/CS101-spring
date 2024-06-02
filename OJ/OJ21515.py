# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:20:50 2024

@author: Lenovo
"""

from heapq import heappush,heappop
class Edge:
    def __init__(self,d,l):
        self.d=d
        self.l=l
    
    def __lt__(self,other):
        return self.l<other.l

n,p,k=map(int,input().split())
dic={i:[] for i in range(1,n+1)}
for i in range(p):
    a,b,l=map(int,input().split())
    dic[a].append(Edge(b,l))
    dic[b].append(Edge(a,l))
ans=float("inf")
mind=[[float("inf")]*(k+1) for i in range(n+1)]
vis=[[False]*(k+1) for i in range(n+1)]
q=[]
heappush(q,(0,1,0))
mind[1][0]=0
while q:
    x,s,num=heappop(q)
    if vis[s][num]:continue
    vis[s][num]=True
    for edge in sorted(dic[s]):
        d,l=edge.d,edge.l
        if mind[d][num]>max(l,x):
            mind[d][num]=max(l,x)
            heappush(q,(mind[d][num],d,num))
        if num<k and mind[d][num+1]>x:
            mind[d][num+1]=mind[s][num]
            heappush(q,(mind[d][num+1],d,num+1))
ans=min(ans,min(mind[n]))
print(ans if ans!=float("inf") else -1)