# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:36:36 2024

@author: Lenovo
"""

n,m=map(int,input().split())
graph={i:set() for i in range(n)}
indegree=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    graph[a].add(b)
    indegree[b]+=1
vis=set()
ind=0
cnt=0
while len(vis)<n:
    for i in range(n):
        if indegree[i]==ind:
            vis.add(i)
            break
    for j in range(n):
        if j not in vis and j not in graph[i]:
            cnt+=1
            indegree[j]+=1
    ind+=1
print(cnt)