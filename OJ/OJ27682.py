# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:45:46 2024

@author: Lenovo
"""

class Node():
    def __init__(self):
        self.parent=None
        self.lchild=None
        self.rchild=None

n=int(input())
tree=[Node() for i in range(n+1)]
d,num=[0]*(n+1),0
for i in range(n):
    l,r=map(int,input().split())
    if l==-1 and r==-1:
        num+=1
    else:
        d[i]=max(d[l],d[r])+1
    node=i
    while tree[node].parent is not None:
        if d[tree[node].parent]<d[node]+1:
            d[tree[node].parent]=d[node]+1
            node=tree[node].parent
        else:
            break
    tree[i].lchild,tree[i].rchild=l,r
    tree[l].parent=tree[r].parent=i
print(max(d),num)