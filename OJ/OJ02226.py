# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:51:35 2024

@author: Lenovo
"""

def check(num):
    for i in range(1,cnt2+1):
        if not vis[i] and fit[num][i]:
            vis[i]=1
            if belong[i]==-1 or check(belong[i]):
                belong[i]=num
                return True
    return False

r,c=map(int,input().split())
maze=[list(input()) for i in range(r)]
row=[[0]*c for i in range(r)]
col=[[0]*c for i in range(r)]
cnt1=cnt2=0
for i in range(r):
    j=0
    while j<c:    
        if maze[i][j]=="*":
            cnt1+=1
        while j<c and maze[i][j]=="*":
            row[i][j]=cnt1
            j+=1
        j+=1
for i in range(c):
    j=0
    while j<r:    
        if maze[j][i]=="*":
            cnt2+=1
        while j<r and maze[j][i]=="*":
            col[j][i]=cnt2
            j+=1
        j+=1
fit=[[0]*(cnt2+1) for _ in range(cnt1+1)]
belong=[-1]*(cnt2+1)
for i in range(r):
    for j in range(c):
        if maze[i][j]=="*":
            l,s=row[i][j],col[i][j]
            fit[l][s]=1
ans=0
for i in range(1,cnt1+1):
    vis=[0]*(cnt2+1)
    if check(i):
        ans+=1
print(ans)