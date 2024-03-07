# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:11:03 2024

@author: Lenovo
"""

from collections import deque
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    stack=[]
    q=deque([i for i in range(1,n+1)])
    count=0
    while q:
        num=q.popleft()
        count+=1
        if count==m:
            stack.append(num)
            count=0
        else:
            q.append(num)
    print(stack[-1])