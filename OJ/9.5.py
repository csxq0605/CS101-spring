# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:12:41 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.height=1
        self.lchild=None
        self.rchild=None

def getheight(root):
    if root is None:
        return 0
    return root.height

def updateheight(root):
    root.height=max(getheight(root.lchild),getheight(root.rchild))+1

def balancefactor(root):
    return getheight(root.lchild)-getheight(root.rchild)

def R(root):
    temp=root.lchild
    root.lchild=temp.rchild
    temp.rchild=root
    updateheight(root)
    updateheight(temp)
    return temp

def L(root):
    temp=root.rchild
    root.rchild=temp.lchild
    temp.lchild=root
    updateheight(root)
    updateheight(temp)
    return temp

def insert(root,num):
    if root is None:    
        return Node(num)
    if num<root.value:
        root.lchild=insert(root.lchild,num)
        updateheight(root)
        if balancefactor(root)==2:
            if balancefactor(root.lchild)==1:
                root=R(root)
            elif balancefactor(root.lchild)==-1:
                root.lchild=L(root.lchild)
                root=R(root)
    else:
        root.rchild=insert(root.rchild,num)
        updateheight(root)
        if balancefactor(root)==-2:
            if balancefactor(root.rchild)==-1:
                root=L(root)
            elif balancefactor(root.rchild)==1:
                root.rchild=R(root.rchild)
                root=L(root)
    return root

def preorder(root):
    ans=[]
    if root is None:
        return []
    ans.append(root.value)
    ans.extend(preorder(root.lchild))
    ans.extend(preorder(root.rchild))
    return ans

n=int(input())
l=list(map(int,input().split()))
tree=None
for num in l:
    tree=insert(tree,num)
print(*preorder(tree))