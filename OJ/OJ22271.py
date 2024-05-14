# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:58:30 2024

@author: Lenovo
"""

n=int(input())
dic={}
for i in range(n):
    t=input()
    dic[t]=dic.get(t,0)+1
for tree in sorted(dic.keys()):
    ans=(dic[tree]/n)*100
    print(tree,"%.4f"%ans+"%")