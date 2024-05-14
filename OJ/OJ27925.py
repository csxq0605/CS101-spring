# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:25:37 2024

@author: Lenovo
"""

from collections import deque
t=int(input())
dic,vis={},[0]*t
for i in range(t):
    l=list(input().split())
    for stu in l:
        dic[stu]=i
cnt,ind,queue=0,{},[]
while True:
    s=input().split()
    if s[0]=="STOP":
        break
    elif s[0]=="DEQUEUE":
        num=queue[cnt].popleft()
        group=dic.get(num,0)
        if not group:
            cnt+=1
            print(num)
            continue
        vis[group]-=1
        if not vis[group]:
            cnt+=1
        print(num)
    else:
        num=s[1]
        group=dic.get(num,0)
        if not group:
            queue.append(deque([num]))
        elif vis[group]:
            queue[ind[group]].append(num)
        else:
            ind[group]=len(queue)
            queue.append(deque([num]))
        vis[group]+=1