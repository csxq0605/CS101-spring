# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:32:31 2023

@author: Lenovo
"""

def common(x,y):
    if x==y:
        return x
    if x>y:
        return common(x//2,y)
    return common(x,y//2)

m,n=map(int,input().split())
print(common(m,n))