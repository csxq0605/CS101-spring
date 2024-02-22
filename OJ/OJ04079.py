# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:17:36 2024

@author: Lenovo
"""

class Node:
    def __init__(self,x):
        self.x=x
        self.lchild=None
        self.rchild=None
        self.parent=None

def tree(l):
    trees[0].x=0 
    for i in range(1,len(l)+1):
        num=l[i-1]
        node=0
        while True:
             if num>trees[node].x:
                 if trees[node].rchild is None:
                     trees[node].rchild=i
                     trees[i].x=num
                     trees[i].parent=node
                     break
                 else:    
                     node=trees[node].rchild
             elif num<trees[node].x:
                 if trees[node].lchild is None:
                     trees[node].lchild=i
                     trees[i].x=num
                     trees[i].parent=node
                     break
                 else:    
                     node=trees[node].lchild
             else:
                 break

def Print(node):
    if node!=0:    
        print(trees[node].x,end=" ")
    if trees[node].lchild is not None:    
        Print(trees[node].lchild)
    if trees[node].rchild is not None:
        Print(trees[node].rchild)

l=list(map(int,input().split()))
trees=[Node("") for i in range(len(l)+1)]
tree(l)
Print(0)