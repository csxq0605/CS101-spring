# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:39:43 2024

@author: Lenovo
"""

from collections import deque
n=int(input())
q=deque([1])
d={1: 1}
maxd=1
for _ in range(n):
    c=q.popleft()
    a,b=map(int,input().split())
    if a!=-1:
        d[a]=d[c]+1
        maxd=max(maxd,d[a])
        q.append(a)
    if b!=-1:
        d[b]=d[c]+1
        maxd=max(maxd,d[b])
        q.append(b)
print(maxd)