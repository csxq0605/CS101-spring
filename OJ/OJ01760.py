# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:46:13 2024

@author: Lenovo
"""

def Print(s,cnt,path):
    ls=sorted(s)
    for items in ls:
        print(" "*cnt+items)
        if dic[path+items]:
            Print(dic[path+items],cnt+1,path+items)

from collections import defaultdict
n=int(input())
s=set()
dic=defaultdict(set)
for _ in range(n):
    l=list(input().split("\\"))
    if l[0] not in s:
        s.add(l[0])
    for i in range(1,len(l)):
        dic["".join(l[:i])].add(l[i])
Print(s,0,"")