# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:25:05 2024

@author: Lenovo
"""

def loge(mid,last,length):
    if length==0:
        return
    if length==1:
        print(mid,end="")
        return
    top=last[-1]
    print(top,end="")
    for i in range(length-1,-1,-1):
        if mid[i]==top:
            break
    loge(mid[:i],last[:i],i)
    loge(mid[i+1:],last[i:-1],length-i-1)

mid=input()
last=input()
length=len(mid)
loge(mid,last,length)