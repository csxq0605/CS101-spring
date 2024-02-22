# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:45:09 2024

@author: Lenovo
"""

from collections import deque
while True:
    n=int(input())
    if n==0:
        break
    q=deque()
    vis=set()
    q.append((1,1))
    vis.add(1)
    while q:
        r,num=q.popleft()
        if r==0:
            print(num)
            break
        for i in range(2):
            dr=(r*10+i)%n
            if dr not in vis:
                vis.add(dr)
                q.append((dr,num*10+i))