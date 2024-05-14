# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:01:49 2024

@author: Lenovo
"""

class DisjSet:
    def __init__(self,n):
        self.pre=[i for i in range(n+1)]
    
    def find(self,x):
        if x==self.pre[x]:
            return x
        self.pre[x]=self.find(self.pre[x])
        return self.pre[x]

    def union(self,x,y):
        rootx,rooty=self.find(x),self.find(y)
        if rootx==rooty:
            return True
        else:
            self.pre[rooty]=rootx
            return False
    
while True:
    try:
        n,m=map(int,input().split())
        s=DisjSet(n)
        for i in range(m):
            x,y=map(int,input().split())
            flag=s.union(x,y)
            print("Yes" if flag else "No")
        count,ans=0,[]
        for i in range(1,n+1):
            if i==s.pre[i]:
                count+=1
                ans.append(i)
        print(count)
        print(*ans)
    except EOFError:
        break