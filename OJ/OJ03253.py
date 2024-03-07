# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:24:33 2024

@author: Lenovo
"""

from collections import deque
while True:
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:
        break
    stack=[]
    q=deque([str(i) for i in range(p,n+1)]+[str(i) for i in range(1,p)])
    count=0
    while q:
        num=q.popleft()
        count+=1
        if count==m:
            stack.append(num)
            count=0
        else:
            q.append(num)
    print(",".join(stack))