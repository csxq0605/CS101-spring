# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:12:33 2024

@author: Lenovo
"""

n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in range(m):
    function,num=input().split()
    if function=="C":
        l=[(x+int(num))%65536 for x in l]
    else:
        ans=0
        num=1<<int(num)
        for x in l:
            if x&num:
                ans+=1
        print(ans)