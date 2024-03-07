# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:40:31 2024

@author: Lenovo
"""

n=int(input())
stack=[]
while n:
    stack.append(str(n%8))
    n//=8
print("".join(stack[::-1]))