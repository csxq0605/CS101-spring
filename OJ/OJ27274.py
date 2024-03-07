# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 08:45:06 2024

@author: Lenovo
"""

from math import log2
s=" "+input()
l,r=0,int(log2(len(s)-1))
ans=""
while l<=r:
    ans+=s[2**l]
    l+=1
    if l>r:
        break
    ans+=s[2**r]
    r-=1
print(ans)