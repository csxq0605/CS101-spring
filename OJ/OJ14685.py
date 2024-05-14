# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:31:31 2024

@author: Lenovo
"""

k,n=map(int,input().split())
dic={}
for i in range(n):
    num=int(input())
    dic[num]=dic.get(num,0)+1
ans=0
l=sorted(dic.keys())
vis=set()
for num in l:
    if dic.get(k-num,0):
        if num==k-num and dic[num]==1:
            break
        if (num,k-num) not in vis and (k-num,num) not in vis:
            vis.add((num,k-num))
        else:
            break
if vis:
    for i in sorted(vis):
        print(*i)
else:
    print("No Solution")