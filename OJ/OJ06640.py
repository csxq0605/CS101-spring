# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:19:11 2024

@author: Lenovo
"""

from collections import defaultdict
n=int(input())
dic=defaultdict(set)
for i in range(1,n+1):
    l=input().split()
    for word in l[1:]:
        dic[word].add(i)
m=int(input())
for i in range(m):
    word=input()
    if dic[word]:
        print(*sorted(dic[word]))
    else:
        print("NOT FOUND")