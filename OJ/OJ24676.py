# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:08:16 2024

@author: Lenovo
"""

import heapq
while True:
    n=int(input())
    if n==0:
        break
    ans=[(x,"",i) for i,x in enumerate(map(int,input().split()))]
    for _ in range(n-1):
        l=list(map(int,input().split()))
        heap=[]
        for i in range(n):
            for num,path,j in ans:
                heap.append((num+l[(i+j)%n],path+str(i),j))
        ans=heap.copy()
    count={}
    dic={}
    heapq.heapify(ans)
    while ans:
        num,path,j=heapq.heappop(ans)
        count[path]=count.get(path,0)+1
        dic[path]=max(dic.get(path,0),num)
        if count[path]==n:
            break
    print(dic[path])