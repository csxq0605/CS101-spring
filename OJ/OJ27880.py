# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:43:29 2024

@author: Lenovo
"""

class Edge:
    def __init__(self,u,v,c):
        self.u,self.v,self.c=u,v,c
    
    def __lt__(self,other):
        return self.c<other.c

class DisjSet:
    def __init__(self,n):
        self.pre=[i for i in range(n+1)]
    
    def find(self,x):
        if x!=self.pre[x]:
            self.pre[x]=self.find(self.pre[x])
        return self.pre[x]
    
    def union(self,x,y):
        rootx,rooty=self.find(x),self.find(y)
        if rootx!=rooty:
            self.pre[rooty]=rootx

n,m=map(int,input().split())
graph=[]
s=DisjSet(n)
for i in range(m):
    u,v,c=map(int,input().split())
    graph.append(Edge(u,v,c))
graph.sort()
cnt=0
for edge in graph:
    u,v,c=edge.u,edge.v,edge.c
    if s.find(u)!=s.find(v):
        cnt+=1
        s.union(u,v)
    if cnt==n-1:
        print(cnt,c)
        break