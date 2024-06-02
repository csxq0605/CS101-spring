# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:55:54 2024

@author: Lenovo
"""

from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=deque()
    ans=0
    for i in range(n):
        if a[i]<b[i]:
            l.append(b[i])
            if a[i]>=l[0]:
                l.popleft()
    print(len(l))