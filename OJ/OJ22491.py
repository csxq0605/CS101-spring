# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:15:13 2024

@author: Lenovo
"""

h=int(input())
m=int(input())
t=2*h-0.5*m
l=[]
for i in range(m):
    s,c=map(float,input().split())
    l.append([s*c,s,c])
l.sort(reverse=True)
ans=i=0
while t and i<m:
    ans+=l[i][0]*min(5/l[i][1],t)
    t-=min(5/l[i][1],t)
    i+=1
print("%.1f"%ans)