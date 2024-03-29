# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 00:17:11 2024

@author: Lenovo
"""

from heapq import heappop,heappush
n=int(input())
heap=[]
for i in range(n):
    func=input().split()
    if func[0]=="2":
        print(heappop(heap))
    else:
        heappush(heap,int(func[1]))