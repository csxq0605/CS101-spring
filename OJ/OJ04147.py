# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:12:15 2024

@author: Lenovo
"""

def hanoitower(n,fro,mid,to,No):
    if n==1:
        print(f"{No}:{fro}->{to}")
        return
    hanoitower(n-1,fro,to,mid,No)
    print(f"{No+n-1}:{fro}->{to}")
    hanoitower(n-1,mid,fro,to,No)

n,a,b,c=input().split()
n=int(n)
hanoitower(n,a,b,c,1)