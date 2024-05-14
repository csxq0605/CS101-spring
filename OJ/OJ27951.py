# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:10:39 2024

@author: Lenovo
"""

from collections import deque
m,n=map(int,input().split())
l=list(map(int,input().split()))
s=set()
queue=deque()
length=ans=0
for num in l:
    if num not in s and length<m:
        ans+=1
        length+=1
        s.add(num)
        queue.append(num)
    elif num not in s and length==m:
        s.add(num)
        queue.append(num)
        ans+=1
        p=queue.popleft()
        s.discard(p)
print(ans)