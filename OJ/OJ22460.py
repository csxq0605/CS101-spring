# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:01:49 2024

@author: Lenovo
"""

ind=0
def build():
    global ind
    if ind>=n or l[ind]=="#":
        ind+=1
        return
    ind+=1
    build()
    build()
    
while True:
    n=int(input())
    if n==0:
        break
    l=list(input().split())
    ind=0
    build()
    print("T" if ind==n else "F")