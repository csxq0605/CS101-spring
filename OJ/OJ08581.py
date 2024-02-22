# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:35:56 2024

@author: Lenovo
"""

class Node:
    def __init__(self):
        self.value=None
        self.lchild=None
        self.rchild=None

def build():
    node=Node()
    node.value=l.pop(0)
    return node
    
def Tree(root):
    if root.value==".":
        return
    root.lchild=build()
    Tree(root.lchild)
    root.rchild=build()
    Tree(root.rchild)
    
def midorder(tree):
    if tree.value==".":
        return
    midorder(tree.lchild)
    print(tree.value,end="")
    midorder(tree.rchild)

def lastorder(tree):
    if tree.value==".":
        return
    lastorder(tree.lchild)
    lastorder(tree.rchild)
    print(tree.value,end="")
    
l=list(input())
tree=build()
Tree(tree)
midorder(tree)
print()
lastorder(tree)
print()