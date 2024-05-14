# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:24:43 2024

@author: Lenovo
"""

from functools import lru_cache
@lru_cache(maxsize=None)
def split(n,x1,y1,x2,y2):
    if n==1:
        ans=sum(sum(i[y1:y2+1]) for i in matrix[x1:x2+1])
        return ans*ans
    ans=float("inf")
    for i in range(x1,x2):
        ans=min(ans,split(n-1,x1,y1,i,y2)+split(1,i+1,y1,x2,y2))
        ans=min(ans,split(1,x1,y1,i,y2)+split(n-1,i+1,y1,x2,y2))
    for i in range(y1,y2):
        ans=min(ans,split(n-1,x1,y1,x2,i)+split(1,x1,i+1,x2,y2))
        ans=min(ans,split(1,x1,y1,x2,i)+split(n-1,x1,i+1,x2,y2))
    return ans

n=int(input())
matrix=[list(map(int,input().split())) for i in range(8)]
s=sum(sum(i) for i in matrix)
ans=split(n,0,0,7,7)
print("%.3f"%(ans/n-s*s/(n*n))**0.5)