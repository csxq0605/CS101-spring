# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:40:17 2024

@author: Lenovo
"""

def swag(num):
    l=len(bin(num))-2
    tmp=[]
    for i in range(l-1,-1,-1):
        if i==1 and (1<<i)&num:
            tmp.append("2")
        elif i==0 and (1<<i)&num:
            tmp.append("2(0)")
        elif (1<<i)&num:
            k=swag(i)
            tmp.append(f"2({k})")
    return "+".join(tmp)

n=int(input())
print(swag(n))