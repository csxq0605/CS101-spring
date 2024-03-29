# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:19:10 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.childs=[]

def build(s):
    if '(' not in s:
        return Node(s)
    root=Node(s[0])
    subtrees=s[2:-1]
    stack=[]
    comma=[-1]
    for i,char in enumerate(subtrees):
        if char=='(':
            stack.append(char)
        elif char==')':
            stack.pop()
        elif char==',' and not stack:
            comma.append(i)
    comma.append(len(subtrees))
    for i in range(len(comma)-1):
        root.childs.append(build(subtrees[comma[i]+1:comma[i+1]]))
    return root

def preorder(root):
    print(root.value,end="")
    for child in root.childs:    
        preorder(child)

def postorder(root):
    for child in root.childs:
        postorder(child)
    print(root.value,end="")

tree=build(input())
preorder(tree)
print()
postorder(tree)
print()