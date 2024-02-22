# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:10:17 2024

@author: Lenovo
"""

from collections import defaultdict
l=list(map(int,input().split()))
k=int(input())
count=defaultdict(int)
count[0]=1
summ=ans=0
for num in l:
    summ+=num
    ans+=count[summ-k]
    count[summ]+=1
print(ans)