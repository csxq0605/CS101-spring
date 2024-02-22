# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:22:05 2024

@author: Lenovo
"""

from collections import deque
class Node:
    def __init__(self):
        self.value=None
        self.degree=0
        self.childs=[]

def build():
    node=Node()
    node.value=l.pop(0)
    node.degree=int(l.pop(0))
    return node

def Tree():
    root=build()
    q=deque([root])
    while q:
        node=q.popleft()
        for i in range(node.degree):
            child=build()
            node.childs.append(child)
            q.append(child)
    return root

def lastorder(tree):
    for child in tree.childs:
        lastorder(child)
    print(tree.value,end=" ")

n=int(input())
for _ in range(n):
    l=list(input().split())
    tree=Tree()
    lastorder(tree)