# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:23:13 2023

@author: Lenovo
"""

move=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
flag=False
def dfs(x,y,step):
    global flag
    if step==p*q:
        flag=True
        return
    for i in range(8):
        dx,dy=x+move[i][0],y+move[i][1]
        if 1<=dx<=q and 1<=dy<=p and not visited[dx][dy] and not flag:
            visited[dx][dy]=True
            ans[step]=chr(dx+64)+str(dy)
            dfs(dx,dy,step+1)
            visited[dx][dy]=False

n=int(input())
for m in range(1,n+1):
    p,q=map(int,input().split())
    flag=False
    ans=["" for _ in range(p*q)]
    visited=[[False]*(p+1) for k in range(q+1)]
    visited[1][1]=True
    ans[0]="A1"
    dfs(1,1,1)
    if flag:
        print(f"Scenario #{m}:")
        print("".join(ans))
        print()
    else:
        print(f"Scenario #{m}:")
        print("impossible")
        print()