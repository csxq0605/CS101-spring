# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:00:55 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value=0):
        self.value=value
        self.lchild=None
        self.rchild=None

def build(tree):
    stack=[]
    num=""
    for char in tree:
        if char=="[":
            if num:    
                stack.append(Node(int(num)))
            num=""
            stack.append(char)
        elif char=="]":
            subtree=[char]
            while stack[-1]!="[" and stack:
                subtree.append(stack.pop())
            subtree.append(stack.pop())
            if len(subtree)==2:
                continue
            if not stack:
                break
            parent=stack[-1]
            if parent.lchild is None:
                parent.lchild=subtree[1]
            else:
                parent.rchild=subtree[1]
        else:
            num+=char
    return subtree[1]

def search(root,summ):
    if root is None:
        return False
    summ+=root.value
    if root.lchild is None and root.rchild is None:
        return summ==I
    left=search(root.lchild,summ)
    right=search(root.rchild,summ)
    return left or right

while True:
    try:
        s=input().split()
    except EOFError:
        break
    I=int(s[0])
    tree=("").join(s[1:])
    tree=tree.replace("(",",[").replace(")","]")
    while True:
        try:
            tree=eval(tree[1:])
            break
        except SyntaxError:
            s=input().split()
            s=("").join(s)
            tree+=s.replace("(",",[").replace(")","]")
    tree=str(tree).replace(", [","[")
    if tree=="[]":
        print("no")
        continue
    tree=build(tree)
    print("yes" if search(tree,0) else "no")