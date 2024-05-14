# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 01:03:44 2024

@author: Lenovo
"""

def dfs(n,start,path):
    if n==0:
        path.sort()
        res.append(path)
        return
    for i in range(start,0,-2):
        if i>n:
            continue
        dfs(n-i,i-2,path+[i])

n=int(input())
res=[]
dfs(n,n if n%2==1 else n-1,[])
res.sort()
for r in res:
    print(' '.join(map(str, r)))
print(len(res))