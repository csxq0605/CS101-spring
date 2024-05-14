# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:48:08 2024

@author: Lenovo
"""

def order(root):
    if dic[root] is None:
        print(root)
        return
    l=dic[root]
    l.append(root)
    l.sort()
    for num in l:
        if num==root:
            print(num)
        else:
            order(num)

n=int(input())
dic,vis1,vis2={},set(),set()
for i in range(n):
    l=list(map(int,input().split()))
    if len(l)==1:
        dic[l[0]]=None
    else:
        dic[l[0]]=l[1:]
        for x in l[1:]:    
            vis2.add(x)
    for x in l:        
        vis1.add(x)
for x in (vis1-vis2):
    root=x
order(root)