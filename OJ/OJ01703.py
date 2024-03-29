# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:43:39 2024

@author: Lenovo
"""

class DisjSet:
    def __init__(self,n):
        self.father=[i for i in range(n+1)]
        self.relation=[0]*(n+1)
    
    def find(self,x):
        if x==self.father[x]:
            return x
        tmp=self.find(self.father[x])
        self.relation[x]=(self.relation[self.father[x]]+self.relation[x])%2
        self.father[x]=tmp
        return self.father[x]
    
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        self.father[rootx]=rooty
        if self.relation[y]==0:
            self.relation[rootx]=1-self.relation[x]
        else:
            self.relation[rootx]=self.relation[x]
    
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=DisjSet(n)
    for i in range(m):
        l=input().split()
        if l[0]=="D":
            s.union(int(l[1]),int(l[2]))
        else:
            root1=s.find(int(l[1]))
            root2=s.find(int(l[2]))
            if root1!=root2:
                print("Not sure yet.")
            elif s.relation[int(l[1])]==s.relation[int(l[2])]:
                print("In the same gang.")
            else:
                print("In different gangs.")