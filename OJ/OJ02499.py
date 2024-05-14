# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:03:57 2024

@author: Lenovo
"""

n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    countl=countr=0
    while a!=1 or b!=1:
        if a==1:
            countr+=b-1
            break
        elif b==1:
            countl+=a-1
            break
        if a>b:
            countl+=a//b
            a=a%b
        else:
            countr+=b//a
            b=b%a
    print(f"Scenario #{i}:")
    print(countl,countr)
    print()