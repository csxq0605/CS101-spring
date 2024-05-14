# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:43:43 2024

@author: Lenovo
"""

from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None

def build(tree):
    for i in range(1,n+1):
        a,b=map(int,input().split())
        tree[i].lchild=a
        tree[i].rchild=b

def out(tree):
    ans=[]
    q1,q2=deque(),deque()
    q1.append(tree[1])
    while q1:
        ans.append(q1[-1].value)
        while q1:
            node=q1.popleft()
            if node.lchild!=-1:
                q2.append(tree[node.lchild])
            if node.rchild!=-1:
                q2.append(tree[node.rchild])
        q1,q2=q2,deque()
    print(*ans)
    
n=int(input())
tree=[Node(i) for i in range(n+2)]
build(tree)
out(tree)