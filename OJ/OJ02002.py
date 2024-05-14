# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:19:33 2024

@author: Lenovo
"""

while True:
    n=int(input())
    if n==0:
        break
    l=[tuple(map(int,input().split())) for i in range(n)]
    s=set(l)
    ans=0
    for i in range(n-1):
        for j in range(i+1,n):
            x1,y1=l[i]
            x2,y2=l[j]
            if (x1+(y1-y2),y1+(x2-x1)) in s and (x2+(y1-y2),y2+(x2-x1)) in s:
                ans+=1
            if (x1-(y1-y2),y1-(x2-x1)) in s and (x2-(y1-y2),y2-(x2-x1)) in s:
                ans+=1
    print(ans//4)