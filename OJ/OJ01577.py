# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:43:35 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None
ans,l,flag=[],[],True

def insert(root,char):
    if root is None:
        return Node(char)
    if root.value>char:
        root.lchild=insert(root.lchild,char)
    else:
        root.rchild=insert(root.rchild,char)
    return root

def preorder(root):
    global ans
    if root is None:
        return
    ans.append(root.value)
    preorder(root.lchild)
    preorder(root.rchild)

def main(l):
    global ans
    tree=None
    for level in l[::-1]:
        for char in level:
            tree=insert(tree,char)
    preorder(tree)
    print("".join(ans))

while flag:
    s=list(input())
    if s==["$"]:
        flag=False
        main(l)
        l,ans=[],[]
    elif s==["*"]:
        main(l)
        l,ans=[],[]
    else:
        l.append(s)