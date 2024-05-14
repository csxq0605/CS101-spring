# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:35:30 2024

@author: Lenovo
"""

import heapq
class Node:
    def __init__(self,ind,val,de):
        self.ind=ind
        self.val=val
        self.de=de
    
    def __lt__(self,other):
        if self.val==other.val:
            return self.de<other.de
        return self.val<other.val

n,k=map(int,input().split())
s=" "+input()
l=[0]*(n+1)
dp=[0]*(n+1)
for i in range(1,n+1):
    if s[i]=="H":l[i]=l[i-1]+1
    else:l[i]=l[i-1]-1
heap=[]
heapq.heappush(heap,Node(0,0,0))
for i in range(1,n+1):
    while heap[0].ind+k<i:
        heapq.heappop(heap)
    tmp=heap[0]
    dp[i]=tmp.val+int(l[i]-l[tmp.ind]<=0)
    heapq.heappush(heap,Node(i,dp[i],l[i]))
print(dp[n])