# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:09:18 2024

@author: Lenovo
"""

class Edge:
    def __init__(self,f,t,c):
        self.f=f
        self.t=t
        self.cost=c
    def __lt__(self,other):
        return self.cost<other.cost

def find(x,fa):
    if fa[x]==-1:
        return x
    return find(fa[x],fa)

n=int(input())
edges=[]
for i in range(n-1):
    line=list(input().split())
    k=int(line[1])
    for j in range(k):
        ch,cost=line[2*j+2],int(line[2*j+3])
        edges.append(Edge(i,ord(ch)-65,cost))
edges.sort()
fa=[-1]*30
ans=cnt=0
for i in range(len(edges)):
    if cnt==n-1:
        break
    e=edges[i]
    if find(e.f,fa)!=find(e.t,fa):
        ans+=e.cost
        cnt+=1
        fa[find(e.t,fa)]=find(e.f,fa)
print(ans)