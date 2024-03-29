# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:13:13 2024

@author: Lenovo
"""

class DisjSet:
    def __init__(self,n):
        self.pre=[i for i in range(n+1)]
    
    def find(self,a):
        if self.pre[a]==a:
            return a
        self.pre[a]=self.find(self.pre[a])
        return self.pre[a]
    
    def merge(self,a,b):
        roota,rootb=self.find(a),self.find(b)
        if roota!=rootb:
            self.pre[rootb]=roota

num=1
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    s=DisjSet(n)
    ans=0
    for i in range(m):
        a,b=map(int,input().split())
        s.merge(a,b)
    for i in range(1,n+1):
        if s.find(i)==i:
            ans+=1
    print(f"Case {num}: {ans}")
    num+=1