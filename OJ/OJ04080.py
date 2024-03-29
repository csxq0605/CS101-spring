# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:14:04 2024

@author: Lenovo
"""

from heapq import heappop,heappush,heapify
n=int(input())
heap=list(map(int,input().split()))
heapify(heap)
ans=0
while len(heap)>=2:
    a=heappop(heap)
    b=heappop(heap)
    ans+=a+b
    heappush(heap,a+b)
print(ans)