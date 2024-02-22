# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:03:54 2024

@author: Lenovo
"""

def cantor(start,end,times):
    if times==n:
        return
    length=(end-start)//3
    l[start+length:end-length]=map(bool,[False]*length)
    cantor(start,start+length,times+1)
    cantor(end-length,end,times+1)

n=int(input())
l=[True]*pow(3,n)
cantor(0,pow(3,n),0)
for flag in l:    
    print("*" if flag else "-",end="")