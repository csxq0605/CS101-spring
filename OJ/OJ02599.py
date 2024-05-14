# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:49:17 2024

@author: Lenovo
"""

import sys
sys.setrecursionlimit(10<<8)
ans=0
def check(p):
    global ans
    vis.add(p)
    for i in range(1,n+1):
        if maze[p][i] and i not in vis:
            if not check(i):
                ans=i
                return True
    return False

while True:
    try:
        n,k=map(int,input().split())
        maze=[[0]*(n+1) for i in range(n+1)]
        vis=set()
        for i in range(n-1):
            a,b=map(int,input().split())
            maze[a][b]=maze[b][a]=1
        if check(k):
            print(f"First player wins flying to airport {ans}")
        else:
            print("First player loses")
    except EOFError:
        break