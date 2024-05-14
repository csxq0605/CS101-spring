# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:59:58 2024

@author: Lenovo
"""

from heapq import heappush,heappop
t=int(input())
for _ in range(t):
    l=[0]+list(map(int,input().split()))
    m=len(l)-1
    ans=[l[1]]
    h1,h2=[],[]
    num=l[1]
    for i in range(2,m+1):
        if l[i]<=num:
            heappush(h1,-l[i])
        else:
            heappush(h2,l[i])
        if i%2:
            if len(h1)==len(h2):
                ans.append(num)
            elif len(h1)>len(h2):
                heappush(h2,num)
                num=-heappop(h1)
                ans.append(num)
            else:
                heappush(h1,-num)
                num=heappop(h2)
                ans.append(num)
    print(len(ans))
    print(*ans)