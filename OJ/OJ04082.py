# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:56:05 2024

@author: Lenovo
"""

from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None

def build(l):
    no=l.pop(0)
    node=Node(no[0])
    if no[1]=="0":
        node.lchild=build(l)
        node.rchild=build(l)
    return node

def Print(tree):
    q1,q2=deque(),deque()
    ans=[]
    node=tree 
    while node is not None:
        if node.value!="$":
            q2.append(node)
        node=node.rchild
    while q2:
        q1.append(q2.pop())
    while q1:
        node=q1.popleft()
        ans.append(node.value)
        if node.lchild is not None:
            node=node.lchild
            while node is not None:
                if node.value!="$":
                    q2.append(node)
                node=node.rchild
            while q2:
                q1.append(q2.pop())
    return ans
        
n=int(input())
l=list(input().split())
tree=build(l)
print(*Print(tree))