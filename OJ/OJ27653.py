# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:55:51 2024

@author: Lenovo
"""

from math import gcd
l=list(map(int,input().split()))
zi=l[0]*l[3]+l[1]*l[2]
mu=l[1]*l[3]
a=gcd(zi,mu)
ans=str(zi//a)+"/"+str(mu//a)
print(ans)