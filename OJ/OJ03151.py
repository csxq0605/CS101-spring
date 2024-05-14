# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:12:27 2024

@author: Lenovo
"""

import heapq
a,b,c=map(int,input().split())
heap=[]
vis=set()
flag=False
heapq.heappush(heap,(0,0,0,""))
vis.add((0,0))
move=["FILL(1)","FILL(2)","DROP(1)","DROP(2)","POUR(1,2)","POUR(2,1)"]
while heap:
    step,l1,l2,path=heapq.heappop(heap)
    if l1==c or l2==c:
        flag=True
        break
    if l1<a and (a,l2) not in vis:
        heapq.heappush(heap,(step+1,a,l2,path+"0"))
        vis.add((a,l2))
    if l2<b and (l1,b) not in vis:
        heapq.heappush(heap,(step+1,l1,b,path+"1"))
        vis.add((l1,b))
    if l1>0 and (0,l2) not in vis:
        heapq.heappush(heap,(step+1,0,l2,path+"2"))
        vis.add((0,l2))
    if l2>0 and (l1,0) not in vis:
        heapq.heappush(heap,(step+1,l1,0,path+"3"))
        vis.add((l1,0))
    if l1>0 and l2<b and (l1+l2-min(l1+l2,b),min(l1+l2,b)) not in vis:
        heapq.heappush(heap,(step+1,l1+l2-min(l1+l2,b),min(l1+l2,b),path+"4"))
        vis.add((l1+l2-min(l1+l2,b),min(l1+l2,b)))
    if l1<a and l2>0 and (min(l1+l2,a),l1+l2-min(l1+l2,a)) not in vis:
        heapq.heappush(heap,(step+1,min(l1+l2,a),l1+l2-min(l1+l2,a),path+"5"))
        vis.add((min(l1+l2,a),l1+l2-min(l1+l2,a)))
if flag:
    print(step)
    for i in path:
        print(move[int(i)])
else:
    print("impossible")