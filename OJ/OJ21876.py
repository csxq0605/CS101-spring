# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 00:25:52 2024

@author: Lenovo
"""

num=1
while True:
    p,e,i,d=map(int,input().split())
    if p==-1 and e==-1 and i==-1 and d==-1:
        break
    for _ in range(21252):
        if not (p+_)%23 and not (e+_)%28 and not (i+_)%33:
            break
    ans=21252-_
    if ans>d:
        ans-=d
    else:
        ans=ans-d+21252
    print(f"Case {num}: the next triple peak occurs in {ans} days.")
    num+=1