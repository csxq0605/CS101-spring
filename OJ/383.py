# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:40:41 2024

@author: Lenovo
"""

from collections import deque
n,m=map(int,input().split())
value=list(map(int,input().split()))
maze={i:set() for i in range(n)}
for i in range(m):
    a,b=map(int,input().split())
    maze[a].add(b)
    maze[b].add(a)
vis=[0]*n
res=[]
for i in range(n):
    if vis[i]:
        continue
    q=deque([i])
    ans=value[i]
    vis[i]=1
    while q:
        now=q.popleft()
        for Next in maze[now]:
            if not vis[Next]:
                vis[Next]=1
                q.append(Next)
                ans+=value[Next]
    res.append(ans)
print(max(res))