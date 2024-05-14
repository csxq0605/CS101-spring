# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:23:41 2024

@author: Lenovo
"""

move=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
def is_valid(x,y):
    return 1<=x<=n and 1<=y<=n and not visited[x][y]

def get_degree(x,y):
    count=0
    for i in range(8):
        dx,dy=x+move[i][0],y+move[i][1]
        if is_valid(dx,dy):
            count+=1
    return count

def dfs(x,y,step):
    if step==n*n:
        return True
    mindind,mind=-1,9
    for i in range(8):
        dx,dy=x+move[i][0],y+move[i][1]
        if is_valid(dx,dy) and get_degree(dx,dy)<mind:
            mindind=i
            mind=get_degree(dx,dy)
    if mindind!=-1:
        dx,dy=x+move[mindind][0],y+move[mindind][1]
        visited[dx][dy]=True
        if dfs(dx,dy,step+1):
            return True
        visited[dx][dy]=False
    return False

n=int(input())
sr,sc=map(int,input().split())    
visited=[[False]*(n+1) for i in range(n+1)]
visited[sr+1][sc+1]=True
flag=dfs(sr+1,sc+1,1)
print("success" if flag else "fail")