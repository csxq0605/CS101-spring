# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:37:56 2024

@author: Lenovo
"""

def dfs(cnt,l,pos):
    if cnt==target:
        return True
    if l==maxn:
        return dfs(cnt+1,0,0)
    for i in range(pos,n):
        if book[i]==0 and l+a[i]<=maxn:
            book[i]=1
            if dfs(cnt,l+a[i],i):
                return True
            book[i]=0
            if l==0:
                return False
            while i+1<n and a[i+1]==a[i]:
                i+=1
    return False

while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    maxn,summ=max(a),sum(a)
    a.sort(reverse=True)
    while True:
        if summ%maxn==0:
            target=summ//maxn
            book=[0]*(n+1)
            if dfs(0,0,0):
                print(maxn)
                break
        maxn+=1