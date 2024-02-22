# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:31:02 2024

@author: Lenovo
"""

from collections import Counter
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    l=[]
    for i in range(n):
        l.extend(list(map(int,input().split())))
    count=Counter(l)
    x,y=count.most_common(2)
    num,flag=y
    ans=[]
    for i in count.keys():
        if count[i]==flag:
            ans.append(i)
    ans.sort()
    print(*ans)