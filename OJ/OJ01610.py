# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:42:48 2024

@author: Lenovo
"""

from collections import deque
class Node:
    def __init__(self):
        self.value=None
        self.childs=[]

def summ(matrix,n):
    num=0
    for i in range(n):
        num+=sum(matrix[i])
    return num

def build(matrix,n):
    node=Node()
    num=summ(matrix,n)
    if num==0:
        node.value="00"
    elif num==n*n:
        node.value="01"
    else:
        node.value="1"
        node.childs.append(build([matrix[i][:n//2] for i in range(n//2)],n//2))
        node.childs.append(build([matrix[i][n//2:] for i in range(n//2)],n//2))
        node.childs.append(build([matrix[i][:n//2] for i in range(n//2,n)],n//2))
        node.childs.append(build([matrix[i][n//2:] for i in range(n//2,n)],n//2))
    return node

def Print(root):
    dic={"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
    ans=""
    q=deque()
    q.append(root)
    while q:
        node=q.popleft()
        ans+=node.value
        if node.childs:
            for child in node.childs:
                q.append(child)
    ans="0"*(4-len(ans)%4)+ans
    res=""
    for i in range(0,len(ans),4):
        res+=dic[ans[i:i+4]]
    return res

k=int(input())
for _ in range(k):
    n=int(input())
    matrix=[list(map(int,input().split())) for i in range(n)]
    Tree=build(matrix,n)
    ans=Print(Tree)
    print(ans)