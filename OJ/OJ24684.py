# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 00:26:29 2024

@author: Lenovo
"""

from collections import Counter
l=list(map(int,input().split()))
count=Counter(l)
maxn=max(list(count.values()))
ans=[]
for i in count.keys():
    if count[i]==maxn:
        ans.append(i)
ans.sort()
print(*ans)