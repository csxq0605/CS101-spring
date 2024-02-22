# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:51:09 2024

@author: Lenovo
"""

from collections import defaultdict
n=int(input())
for i in range(n):
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    len1,len2=len(l1),len(l2)
    s,dic=set(),defaultdict(int)
    for j in range(1,len1-1,2):
        if l1[j]<0:
            break
        s.add(l1[j])
        dic[l1[j]]+=l1[j-1]
    for j in range(1,len2-1,2):
        if l2[j]<0:
            break
        s.add(l2[j])
        dic[l2[j]]+=l2[j-1]
    s=sorted(s,reverse=True)
    ans=[]
    for num in s:
        if dic[num]==0:
            continue
        ans.append("[ "+str(dic[num])+" "+str(num)+" ]")
    print(*ans)