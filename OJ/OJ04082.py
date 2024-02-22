# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:40:32 2024

@author: Lenovo
"""

from collections import deque
i=index=0
class Node:
    def __init__(self,No):
        self.No=No
        self.left=None
        self.right=None

def node():
    global i
    tree[i].left=None
    tree[i].right=None
    i+=1
    return tree[i-1]

def trees():
    global index
    nodes=node()
    p=l[index]
    index+=1
    nodes.No=p[0]
    if p[1]=="0" and p[0]!="$":
        nodes.left=trees()
        nodes.right=trees()
    return nodes

def decode(nodes):
    s,q=deque(),deque()
    while nodes is not None:
        if nodes.No!="$":
            s.append(nodes)
        nodes=nodes.right
    while s:
        q.append(s.pop())
    while q:
        nodes=q.popleft()
        print(nodes.No,end=" ")
        if nodes.left is not None:
            nodes=nodes.left
            while nodes is not None:
                if nodes.No!="$":
                    s.append(nodes)
                nodes=nodes.right
            while s:
                q.append(s.pop())
                
n=int(input())
l=list(input().split())
tree=[Node("")for i in range(n)]
i=index=0
Tree=trees()
decode(Tree)