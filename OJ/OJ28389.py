# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:36:25 2024

@author: Lenovo
"""

import bisect
n=int(input())
l=list(map(int,input().split()))
cnt=0
had=[]
for i in range(n):
    if not had:
        cnt+=1
        had.append(l[i])
    else:
        if had[-1]<=l[i]:
            had[-1]=l[i]
        else:
            ind=bisect.bisect_right(had,l[i])
            if ind:
                had[ind-1]=l[i]
            else:
                had.insert(0,l[i])
                cnt+=1
print(cnt)