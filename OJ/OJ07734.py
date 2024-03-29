# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:15:26 2024

@author: Lenovo
"""

class DisjSet:
    def __init__(self,n):
        self.pre=[i for i in range(2*n+1)]

    def find(self,x):
        while self.pre[x]!=x:
            self.pre[x]=self.pre[self.pre[x]]
            x=self.pre[x]
        return x

    def merge(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx==rooty:
            return
        else:
            self.pre[rootx]=rooty
        
t=int(input())
for _ in range(1,t+1):
    n,m=map(int,input().split())
    Set=DisjSet(n)
    flag=False
    for i in range(m):
        a,b=map(int,input().split())
        if Set.find(a)==Set.find(b):
            flag=True
        else:
            Set.merge(a,b+n)
            Set.merge(b,a+n)
    print(f"Scenario #{_}:")
    print("Suspicious bugs found!" if flag else "No suspicious bugs found!")
    print()