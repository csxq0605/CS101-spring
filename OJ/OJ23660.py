# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:01:35 2024

@author: Lenovo
"""

n=int(input())
for _ in range(n):
    l=list(map(int,input().split()))
    t,l=l[0],l[1:]
    num=0
    for x in range(2**t):
        summ=0
        for i in range(t):
            if (1<<i)&x:
                summ+=l[i]
        if summ%7==0:
            num+=1
    print(num)