# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:58:45 2024

@author: Lenovo
"""

import heapq
n,k=map(int,input().split())
l=[[0,0]]+[list(map(int,input().split())) for i in range(n)]
heap,res=[],[]
for i in range(1,n+1):
    heapq.heappush(heap,(-l[i][0],i))
for i in range(k):
    num,index=heapq.heappop(heap)
    heapq.heappush(res,(-l[index][1],index))
num,ans=heapq.heappop(res)
print(ans)