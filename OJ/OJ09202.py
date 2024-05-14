# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:57:29 2024

@author: Lenovo
"""

def dfs(x):
    for i in dic[x]:
        if i not in vis:
            indegree[i]-=1
            if not indegree[i]:
                vis.add(i)
                dfs(i)

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    dic={i:[] for i in range(1,n+1)}
    indegree=[0]*(n+1)
    for i in range(m):
        x,y=map(int,input().split())
        dic[x].append(y)
        indegree[y]+=1
    vis=set()
    for i in range(1,n+1):
        if indegree[i]==0 and i not in vis:
            vis.add(i)
            dfs(i)
    flag=False
    for i in range(1,n+1):
        if i not in vis:
            flag=True
            break
    print("Yes" if flag else "No")