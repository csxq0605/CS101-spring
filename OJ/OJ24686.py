# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:43:52 2024

@author: Lenovo
"""

import math
k,n=map(int,input().split())
l1,l2,d=[0]*(1<<k),[0]*(1<<k),[0]+[k-int(math.log2(i)) for i in range(1,1<<k)]
for _ in range(n):
    l=list(map(int,input().split()))
    if l[0]==1:
        x,y=l[1],l[2]
        w=l[2]*((1<<d[x])-1)
        l1[x]+=l[2]
        while x!=1:
            x//=2
            l2[x]+=w
    else:
        x=l[1]
        ans=l1[1]
        while x!=1:
            ans+=l1[x]
            x//=2
        ans=ans*((1<<d[l[1]])-1)+l2[l[1]]
        print(ans)