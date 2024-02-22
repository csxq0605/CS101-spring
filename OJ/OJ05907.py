# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:36:06 2024

@author: Lenovo
"""

class Node:
    def __init__(self):
        self.lchild=None
        self.rchild=None
        self.parent=None

def exchange(x,y):
    px,py=tree[x].parent,tree[y].parent
    if px==py:
        if tree[px].lchild==x:
            tree[px].lchild,tree[px].rchild=y,x
        else:
            tree[px].lchild,tree[px].rchild=x,y
    else:
        if tree[px].lchild==x:
            tree[px].lchild=y
        else:
            tree[px].rchild=y
        tree[y].parent=px
        if tree[py].lchild==y:
            tree[py].lchild=x
        else:
            tree[py].rchild=x
        tree[x].parent=py

def search(x):
    while tree[x].lchild!=-1:
        x=tree[x].lchild
    print(x)

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    tree=[Node() for i in range(n+1)]
    for i in range(n):
        a,la,ra=map(int,input().split())
        tree[a].lchild,tree[a].rchild=la,ra
        tree[la].parent=tree[ra].parent=a
    for i in range(m):
        l=list(map(int,input().split()))
        if l[0]==1:
            x,y=l[1],l[2]
            exchange(x,y)
        else:
            x=l[1]
            search(x)