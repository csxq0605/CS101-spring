# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:57:44 2024

@author: Lenovo
"""

def loge(front,mid,length):
    if length==0:
        return
    if length==1:
        print(front[0],end="")
        return
    top=front[0]
    i=0
    while mid[i]!=top:
        i+=1
    loge(front[1:],mid,i)
    loge(front[i+1:],mid[i+1:],length-i-1)
    print(top,end="")
while True:
    try:
        front,mid=map(str,input().split())
        length=len(front)
        loge(front,mid,length)
        print()
    except:
        break