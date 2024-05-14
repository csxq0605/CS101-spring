# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:09:37 2024

@author: Lenovo
"""

class Edge:
    def __init__(self,s,e,w):
        self.s=s
        self.e=e
        self.w=w
    def __lt__(self,other):
        return self.w<other.w
        
class DisjSet:
    def __init__(self,n):
        self.p=[i for i in range(n)]
        
    def find(self,x):
        if x!=self.p[x]:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    
    def merge(self,x,y):
        xroot,yroot=self.find(x),self.find(y)
        if xroot!=yroot:
            self.p[yroot]=xroot

while True:
    try:
        n=int(input())
        matrix=[list(map(int,input().split())) for i in range(n)]
        l=[]
        for i in range(n):
            for j in range(n):
                l.append(Edge(i,j,matrix[i][j]))
        l.sort()
        s=DisjSet(n)
        ans=cnt=0
        for edge in l:
            if s.find(edge.s)!=s.find(edge.e):
                ans+=edge.w
                s.merge(edge.s,edge.e)
                cnt+=1
            if cnt==n-1:
                break
        print(ans)
    except EOFError:
        break