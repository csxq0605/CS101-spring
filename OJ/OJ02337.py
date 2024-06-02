# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:15:56 2024

@author: Lenovo
"""

import sys
sys.setrecursionlimit(10<<8)
class Edge:
    def __init__(self,s,e,v,word):
        self.s=s
        self.e=e
        self.v=v
        self.word=word
    
    def __lt__(self,other):
        return self.word<other.word

def find(x):
    if x!=pre[x]:
        pre[x]=find(pre[x])
    return pre[x]

def dfs(end):
    for edge in l:
        if not edge.v and edge.s==end:
            edge.v=1
            dfs(edge.e)
            ans.append(edge.word)

t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    pre={chr(i):chr(i) for i in range(97,123)}
    ind={chr(i):0 for i in range(97,123)}
    out={chr(i):0 for i in range(97,123)}
    for i in range(n):
        word=input()
        s,e=word[0],word[-1]
        ind[e]+=1
        out[s]+=1
        l.append(Edge(s,e,0,word))
        fs,fe=find(s),find(e)
        if fs!=fe:
            pre[fe]=fs
    l.sort()
    flag=True
    a=find(l[0].s)
    for i in range(97,123):
        if ind[chr(i)] or out[chr(i)]:
            if a!=find(chr(i)):
                flag=False
                break
    start=l[0].s
    c1=c2=0
    for i in range(97,123):
        if ind[chr(i)]==out[chr(i)]:
            continue
        elif out[chr(i)]-ind[chr(i)]==1:
            c1+=1
            start=chr(i)
        elif ind[chr(i)]-out[chr(i)]==1:
            c2+=1
        else:
            flag=False
            break
    if flag and ((c1==0 and c2==0) or (c1==1 and c2==1)):
        ans=[]
        dfs(start)
        ans=ans[::-1]
    print(".".join(ans) if flag else "***")