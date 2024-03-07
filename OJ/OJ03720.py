# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:38:30 2024

@author: Lenovo
"""

class Node:
    def __init__(self,x,depth):
        self.x=x
        self.depth=depth
        self.lchild=None
        self.rchild=None

def pre_order(tree,index):
    print(tree[index].x,end='')
    if tree[index].lchild is not None and tree[tree[index].lchild].x!='*':
        pre_order(tree,tree[index].lchild)
    if tree[index].rchild is not None and tree[tree[index].rchild].x!='*':
        pre_order(tree,tree[index].rchild)

def mid_order(tree,index):
    if tree[index].lchild is not None and tree[tree[index].lchild].x!='*':
        mid_order(tree,tree[index].lchild)
    print(tree[index].x,end='')
    if tree[index].rchild is not None and tree[tree[index].rchild].x!='*':
        mid_order(tree,tree[index].rchild)

def post_order(tree,index):
    if tree[index].lchild is not None and tree[tree[index].lchild].x!='*':
        post_order(tree,tree[index].lchild)
    if tree[index].rchild is not None and tree[tree[index].rchild].x!='*':
        post_order(tree,tree[index].rchild)
    print(tree[index].x,end='')

n=int(input())
for _ in range(n):
    tree=[]
    p=0
    stack=[]
    while True:
        s=input()
        if s=='0':
            break
        if p==0:
            tree.append(Node(s[-1],len(s)-1))
        else:
            tree.append(Node(s[-1],len(s)-1))
            index=stack[-1]
            while tree[index].depth>=(len(s)-1):
                stack.pop()
                index=stack[-1]
            if tree[index].lchild is None:
                tree[index].lchild=p
            else:
                tree[index].rchild=p
                stack.pop()
        stack.append(p)
        p+=1
    pre_order(tree,0)
    print()
    post_order(tree,0)
    print()
    mid_order(tree,0)
    print()
    print()