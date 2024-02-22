# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:45:54 2024

@author: Lenovo
"""

p=list(map(int,input().split()))
minp,profit=p[0],0
for price in p:
    minp=min(minp,price)
    profit=max(profit,price-minp)
print(profit)