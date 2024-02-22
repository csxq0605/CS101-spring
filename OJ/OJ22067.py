# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:26:47 2024

@author: Lenovo
"""

import heapq
from collections import defaultdict
heap,stack,count=[],[],defaultdict(int)
while True:
    try:
        function=list(input().split())
        if function[0]=="pop":
            if stack:
                count[stack.pop()]-=1
        elif function[0]=="push":
            stack.append(int(function[1]))
            count[int(function[1])]+=1
            heapq.heappush(heap,int(function[1]))
        else:
            if stack:    
                while heap and not count[heap[0]]:
                    heapq.heappop(heap)  
                print(heap[0])
    except EOFError:
        break