# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:15:56 2024

@author: Lenovo
"""

def dfs(string,num):
    if num==n:
        return True
    for s in l:
        if s not in vis and string[-1]==s[0]:
            ans.append(s)
            vis.add(s)
            if dfs(s,num+1):
                return True
            vis.discard(s)
            ans.pop()
    return False

t=int(input())
for _ in range(t):
    n=int(input())
    l=[input() for i in range(n)]
    l.sort()
    flag=False
    for s in l:
        ans=[s]
        vis=set([s])
        if dfs(s,1):
            flag=True
            break
    print(".".join(ans) if flag else "***")