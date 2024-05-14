# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:00:19 2024

@author: Lenovo
"""

import heapq
n=int(input())
word,words={},{}
for i in range(n):
    w=input()
    for p in range(4):
        ws=w[:p]+"_"+w[p+1:]
        word[w]=word.get(w,[])+[ws]
        words[ws]=words.get(ws,[])+[w]
start,end=input().split()
vis=set([start])
heap=[]
flag=False
heapq.heappush(heap,(1,[start]))
while heap:
    l,path=heapq.heappop(heap)
    node=path[-1]
    if node==end:
        flag=True
        break
    for ws in word[node]:
        if ws in vis:
            continue
        vis.add(ws)
        for w in words[ws]:
            if w in vis:
                continue
            vis.add(w)
            heapq.heappush(heap,(l+1,path+[w]))
if flag:            
    print(*path)
else:
    print("NO")