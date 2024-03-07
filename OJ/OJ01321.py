# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:05:35 2023

@author: Lenovo
"""

ans=num=0
def dfs(a):
    global ans,num
    if num==k:
        ans+=1
        return
    for i in range(a+1,n):
        for j in range(n):
            if martix[i][j]=="#" and i not in setx and j not in sety:
                setx.add(i)
                sety.add(j)
                num+=1
                dfs(i)
                num-=1
                setx.remove(i)
                sety.remove(j)

while True:
    n,k=map(int,input().split())
    if n==-1 and k==-1:
        break
    martix=[list(input()) for i in range(n)]
    ans,setx,sety=0,set(),set()
    dfs(-1)
    print(ans)