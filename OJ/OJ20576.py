# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:42:06 2024

@author: Lenovo
"""

class BinaryTree:
    def __init__(self,root):
        self.root=root
        self.lchild=None
        self.rchild=None

def build(list):
    stack,bools=[],[]
    dic={'(':0,'or':1,'and':2,'not':3}
    for word in list:
        if word=='(':
            stack.append(word)
        elif word==')':
            Word=stack.pop()
            while Word!='(':
                bools.append(Word)
                Word=stack.pop()
        elif word=='True' or word=='False':
            bools.append(word)
        else:
            while stack and dic[word]<=dic[stack[-1]]:
                bools.append(stack.pop())
            stack.append(word)
    while stack:
        bools.append(stack.pop())
    stack=[]
    for word in bools:
        if word=='not':  
            node=BinaryTree(word)
            node.lchild=stack.pop()
            stack.append(node)
        elif word=='True' or word=='False':
            stack.append(BinaryTree(word))
        else:
            node=BinaryTree(word)
            node.rchild,node.lchild=stack.pop(),stack.pop()
            stack.append(node)
    Tree=stack[-1]
    return Tree

def Print(Tree):
    if Tree.root=='or':
        return Print(Tree.lchild)+['or']+Print(Tree.rchild)
    elif Tree.root=='not':
        return ['not']+(['(']+Print(Tree.lchild)+[')'] if Tree.lchild.root not in ['True','False'] else Print(Tree.lchild))
    elif Tree.root=='and':
        return (['(']+Print(Tree.lchild)+[')'] if Tree.lchild.root=='or' else Print(Tree.lchild))+['and']+(['(']+Print(Tree.rchild)+[')'] if Tree.rchild.root=='or' else Print(Tree.rchild))
    else:
        return [str(Tree.root)]

bools=list(input().split())
Tree=build(bools)
print(' '.join(Print(Tree)))