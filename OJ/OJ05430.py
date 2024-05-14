# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:55:13 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None

def build(s):
    stack=[]
    ans=""
    w={"(":0,"+":1,"-":1,"*":2,"/":2}
    for char in s:
        if char in "+-*/":
            while stack and w[stack[-1]]>=w[char] and stack[-1]!="(":
                ans+=stack.pop()
            stack.append(char)
        elif char==")":
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.pop()
        elif char=="(":
            stack.append(char)
        else:
            ans+=char
    while stack:
        ans+=stack.pop()
    print(ans)
    stack=[]
    for char in ans:
        if char in "+-*/":
            node=Node(char)
            node.rchild=stack.pop()
            node.lchild=stack.pop()
        else:
            node=Node(char)
        stack.append(node)
    return stack[0]

def getdepth(node):
    ld=getdepth(node.lchild) if node.lchild else 0
    rd=getdepth(node.rchild) if node.rchild else 0
    return max(ld,rd)+1

def Print(node,d):
    maze=[" "*(2**d-1)+node.value+" "*(2**d-1)]
    if d==0:
        return node.value
    maze.append(" "*(2**d-2)+("/" if node.lchild else " ")+" "+("\\" if node.rchild else " ")+" "*(2**d-2))
    left=Print(node.lchild,d-1) if node.lchild else [" "*(2**d-1)]*(2*d-1)
    right=Print(node.rchild,d-1) if node.rchild else [" "*(2**d-1)]*(2*d-1)
    for i in range(2*d-1):
        maze.append(left[i]+" "+right[i])
    return maze

def getval(node):
    if node.value in "+-*/":
        left=str(getval(node.lchild))
        right=str(getval(node.rchild))
        op="//" if node.value=="/" else node.value
        return eval(left+op+right)
    else:
        return dic[node.value]

s=input()
n=int(input())
dic={}
for i in range(n):
    x,num=input().split()
    dic[x]=int(num)
tree=build(s)
d=getdepth(tree)
for l in Print(tree,d-1):
    print(l)
print(getval(tree))