# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:39:09 2024

@author: Lenovo
"""

class Node:
    def __init__(self):
        self.childs={}

class Tree:
    def __init__(self):
        self.root=Node()
    
    def insert(self,l):
        node=self.root
        for direct in l:
            if direct not in node.childs:
                node.childs[direct]=Node()
            node=node.childs[direct]
            
def Print(node,level):
    if not node.childs:
        return
    for direct in sorted(node.childs.keys()):
        print(" "*level+direct)
        Print(node.childs[direct],level+1)
        
n=int(input())
tree=Tree()
for i in range(n):
    l=list(input().split("\\"))
    tree.insert(l)
Print(tree.root,0)