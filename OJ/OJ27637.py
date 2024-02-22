# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:17:26 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None

def build(s):
    if s=='*':
        return None
    if '('not in s:
        return Node(s)
    root=s[0]
    subtrees=s[2:-1]
    stack=[]
    comma=None
    for i,char in enumerate(subtrees):
        if char=='(':
            stack.append(char)
        elif char==')':
            stack.pop()
        elif char==',' and not stack:
            comma=i
            break
    left=subtrees[:comma]if comma is not None else subtrees
    right=subtrees[comma+1:]if comma is not None else None
    root=Node(root)
    root.lchild=build(left)
    root.rchild=build(right)if right is not None else None
    return root

def preorder(root):
    if root is None:
        return ""
    return root.value+preorder(root.lchild)+preorder(root.rchild)

def inorder(root):
    if root is None:
        return ""
    return inorder(root.lchild)+root.value+inorder(root.rchild)

n=int(input())
for _ in range(n):
    tree=build(input())
    print(preorder(tree))
    print(inorder(tree))