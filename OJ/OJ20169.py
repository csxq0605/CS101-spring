# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:30:07 2024

@author: Lenovo
"""

class DisjSet:
    def __init__(self,n):
        self.p=[i for i in range(n+1)]
        
    def find(self,x):
        if x!=self.p[x]:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    
    def merge(self,x,y):
        rootx,rooty=self.find(x),self.find(y)
        if rootx!=rooty:
            self.p[rootx]=rooty

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=DisjSet(n)
    for i in range(m):
        x,y=map(int,input().split())
        if s.find(x)!=s.find(y):
            s.merge(x,y)
    ans=[s.find(i) for i in range(1,n+1)]
    print(*ans)