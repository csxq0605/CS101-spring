# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:10:29 2024

@author: Lenovo
"""

class Trie:
    def __init__(self):
        self.trie=[[0]*10 for _ in range((n+1)*10)]
        self.end=[False]*((n+1)*10)
        self.L=1

def insert_trie(s):
    global flag
    r,i=0,0
    while i<len(s):
        if trie.end[r]:
            flag=False
        j=int(s[i])
        i+=1
        if not trie.trie[r][j]:
            trie.trie[r][j]=trie.L
            trie.L+=1
        r=trie.trie[r][j]
    for i in range(10):
        if trie.trie[r][i]:
            flag=False
    trie.end[r]=True

t=int(input())
for _ in range(t):
    n=int(input())
    trie=Trie()
    trie.L=1
    trie.trie=[[0]*10 for _ in range((n+1)*10)]
    trie.end=[False]*((n+1)*10)
    flag=True
    for _ in range(n):
        tel=input()
        insert_trie(tel)
        
        
        
class TrieNode:
    def __init__(self):
        self.child={}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, nums):
        curnode = self.root
        for x in nums:
            if x not in curnode.child:
                curnode.child[x] = TrieNode()
            curnode=curnode.child[x]

    def search(self, num):
        curnode = self.root
        for x in num:
            if x not in curnode.child:
                return 0
            curnode = curnode.child[x]
        return 1

t = int(input())
p = []
for _ in range(t):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(str(input()))
    nums.sort(reverse=True)
    s = 0
    trie = Trie()
    for num in nums:
        s += trie.search(num)
        trie.insert(num)
    if s > 0:
        print('NO')
    else:
        print('YES')