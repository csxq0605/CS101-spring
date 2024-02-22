# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:05:29 2024

@author: Lenovo
"""

def count(s,length):
    if dp[s][length]!=-1:
        return dp[s][length]
    if length<=1:
        return 0
    if length==2 and l[s]==l[s+1]:
        return 0
    elif length==2:
        return 1
    if l[s]==l[s+length-1]:
        return count(s+1,length-2)
    res=min(length+1,count(s,length-1)+1,count(s+1,length-1)+1,count(s+1,length-2)+1)
    dp[s][length]=res
    return res

l=list(input())
dp=[[-1]*(len(l)+1) for i in range(len(l)+1)]
res=count(0,len(l))
print(res)