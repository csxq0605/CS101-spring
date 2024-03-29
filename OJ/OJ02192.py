# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:31:12 2024

@author: Lenovo
"""

def dfs(ca,cb,cc):
    global flag
    if cc==lc:
        flag=True
        return
    if ca<la and a[ca]==c[cc]:
        dfs(ca+1,cb,cc+1)
        if flag:
            return
    if cb<lb and b[cb]==c[cc]:
        dfs(ca,cb+1,cc+1)
        if flag:
            return

n=int(input())
for i in range(1,n+1):
    a,b,c=input().split()
    la,lb,lc=len(a),len(b),len(c)
    flag=False
    if a[-1]!=c[-1] and b[-1]!=c[-1]:
        flag=False
    elif set(a+b)!=set(c):
        flag=False
    else:
        dfs(0,0,0)
    if flag:
        print(f"Data set {i}: yes")
    else:
        print(f"Data set {i}: no")