# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:35:05 2024

@author: Lenovo
"""

class Node:
    def __init__(self):
        self.childs={}

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self,nums):
        node=self.root
        for x in nums:
            if x not in node.childs:
                node.childs[x]=Node()
            node=node.childs[x]

    def search(self,num):
        node=self.root
        for x in num:
            if x not in node.childs:
                return 0
            node=node.childs[x]
        return 1

t=int(input())
p=[]
for _ in range(t):
    n=int(input())
    nums=[input() for i in range(n)]
    nums.sort(reverse=True)
    flag=False
    trie=Trie()
    for num in nums:
        flag=(flag or trie.search(num))
        trie.insert(num)
    print("NO" if flag else "YES")