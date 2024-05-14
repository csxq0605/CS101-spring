# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:42:27 2024

@author: Lenovo
"""

def preorder(mid,post,l):
    if l<=0:
        return []
    if l==1:
        return mid
    root=post[-1]
    for i in range(l):
        if mid[i]==root:
            break
    left=preorder(mid[:i],post[:i],i)
    right=preorder(mid[i+1:],post[i:-1],l-i-1)
    return [root]+left+right

mid=list(input().split())
post=list(input().split())
ans=preorder(mid,post,len(mid))
print(*ans)