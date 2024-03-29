# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:14:01 2024

@author: Lenovo
"""

def lowbit(x):
    return x&-x

def query(x):
    res=0
    while x>0:
        res+=dic[x]
        x-=lowbit(x)
    return res

def add(x,num):
    while x<=32001:
        dic[x]+=num
        x+=lowbit(x)

n=int(input())
stars=[]
for _ in range(n):
    x,y=map(int,input().split())
    stars.append((x+1,y+1))
stars.sort(key=lambda x:x[1])
dic,ans=[0]*32010,[0]*n
for star in stars:
    t=query(star[0])
    ans[t]+=1
    add(star[0],1)
for i in range(n):
    print(ans[i])