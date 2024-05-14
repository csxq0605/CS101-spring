# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:18:35 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None

def build(s):
    if len(s)==1:
        return Node("B") if s=="0" else Node("I")
    if "0"*len(s)==s:    
        node=Node("B")
    elif "1"*len(s)==s:
        node=Node("I")
    else:
        node=Node("F")
    node.lchild=build(s[0:len(s)//2])
    node.rchild=build(s[len(s)//2:])
    return node

def postorder(root):
    if root is None:
        return
    postorder(root.lchild)
    postorder(root.rchild)
    print(root.value,end="")

n=int(input())
s=input()
tree=build(s)
postorder(tree)