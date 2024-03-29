# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:27:53 2024

@author: Lenovo
"""

from heapq import heappush,heappop
while True:
    a,b,c=map(int,input().split())
    if not a and not b and not c:
        break
    l1,l2,l3=[],[],[]
    while True:
        s=list(input().split())
        if s[0]=="#":
            break
        if s[1]=="1" or s[1]=="2":
            h,m=map(int,s[0].split(":"))
            l1.append((h*60+m,int(s[1])))
        elif s[1]=="3" or s[1]=="4":
            h,m=map(int,s[0].split(":"))
            l2.append((h*60+m,int(s[1])))
        else:
            h,m=map(int,s[0].split(":"))
            l3.append((h*60+m,int(s[1])))
    ans=0
    num,heap=0,[]
    for t in l1:
        if num<a:
           num+=1
           heappush(heap,t[0]+30)
           ans+=t[1]
        else:
            if t[0]+30>=heap[0]:
                ans+=t[1]
                right=heappop(heap)
                heappush(heap,max(right,t[0])+30)
    num,heap=0,[]
    for t in l2:
        if num<b:
           num+=1
           heappush(heap,t[0]+30)
           ans+=t[1]
        else:
            if t[0]+30>=heap[0]:
                ans+=t[1]
                right=heappop(heap)
                heappush(heap,max(right,t[0])+30)
    num,heap=0,[]
    for t in l3:
        if num<c:
           num+=1
           heappush(heap,t[0]+30)
           ans+=t[1]
        else:
            if t[0]+30>=heap[0]:
                ans+=t[1]
                right=heappop(heap)
                heappush(heap,max(right,t[0])+30)
    print(ans)