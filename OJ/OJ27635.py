# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:25:52 2024

@author: Lenovo
"""

def dfs(node,parent):
    vis[node]=True
    for neighbour in dic[node]:
        if not vis[neighbour]:
            if dfs(neighbour,node):
                return True
        elif neighbour!=parent:
            return True
    return False
            
n,m=map(int,input().split())
dic={i:[] for i in range(n)}
for i in range(m):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
vis,flag=[False]*n,False
stack=[0]
vis[0]=True
while stack:
    node=stack.pop()
    for nodes in dic[node]:
        if not vis[nodes]:
            stack.append(nodes)
            vis[nodes]=True
flag=all(vis)
if flag:
    print("connected:yes")
else:
    print("connected:no")
vis,flag=[False]*n,False
for node in range(n):
    if not vis[node] and dfs(node,-1):
        flag=True
        break
if flag:
    print("loop:yes")
else:
    print("loop:no")