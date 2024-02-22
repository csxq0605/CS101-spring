# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:31:45 2024

@author: Lenovo
"""

l=[-1]+[int(i) for i in input()]+[-1]
ans=pre=now=0
for i in range(1,len(l)):
    if l[i]==l[i-1]:
        now+=1
    else:
        ans+=min(pre,now)
        pre=now
        now=1
print(ans)