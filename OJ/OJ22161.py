# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:13:33 2024

@author: Lenovo
"""

import heapq
def tree(line):
    queue=[]
    for s,w in line:
        heapq.heappush(queue,[w,s,None,None])
    while len(queue)>=2:
        left=heapq.heappop(queue)
        right=heapq.heappop(queue)
        parent=[left[0]+right[0],None,left,right]
        heapq.heappush(queue,parent)
    return queue[0]

def firstencode(Tree):
    codes={}
    def check(node,code):
        if node[1]:
            codes[node[1]]=code
        else:
            check(node[2],code+"0")
            check(node[3],code+"1")
    check(Tree,"")
    return codes

def encoding(string):
    encode=""
    for i in string:
        encode+=codes[i]
    return encode

def decoding(string):
    decode=""
    node=Tree
    for num in string:
        if num=="0":
            node=node[2]
        else:
            node=node[3]
        if node[1]:
            decode+=node[1]
            node=Tree
    return decode

n=int(input())
line=[]
for i in range(n):
    s,w=input().split()
    w=int(w)
    line.append((s,w))
Tree=tree(line)
codes=firstencode(Tree)
while True:
    try:
        string=input()
        if string[0] in ["0","1"]:
            print(decoding(string))
        else:
            print(encoding(string))
    except:
        break