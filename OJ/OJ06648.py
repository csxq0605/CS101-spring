# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:59:58 2024

@author: Lenovo
"""

import heapq
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    ans=sorted(list(map(int,input().split())))
    for i in range(m-1):
        l=sorted(list(map(int,input().split())))
        heap,res,cnt=[],[],0
        for j in range(n):
            heapq.heappush(heap,(ans[j]+l[0],j,0))
        while True:
            num,x,y=heapq.heappop(heap)
            res.append(num)
            cnt+=1
            if cnt==n:
                break
            heapq.heappush(heap,(ans[x]+l[y+1],x,y+1))
        ans=res.copy()
    print(*ans)