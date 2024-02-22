# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:58:58 2024

@author: Lenovo
"""

s=input()
x=y=0
d=[0,1]
for char in s:
    if char=="G":
        x+=d[0]
        y+=d[1]
    elif char=="R":
        d=[d[1],-d[0]]
    else:
        d=[-d[1],d[0]]
print(int((x==0 and y==0)or(d!=[0,1])))