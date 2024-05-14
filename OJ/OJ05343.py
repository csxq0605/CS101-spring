# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:27:18 2024

@author: Lenovo
"""

n=int(input())
cards=list(input().split())
l=[[] for i in range(10)]
for card in cards:
    l[int(card[1])].append(card)
cards=[]
for i in range(1,10):
    ans=" ".join(l[i])
    cards+=l[i]
    print(f"Queue{i}:{ans}")
l=[[]for i in range(5)]
for card in cards:
    l[ord(card[0])-64].append(card)
cards=[]
for i in range(1,5):
    tmp=chr(i+64)
    ans=" ".join(l[i])
    cards+=l[i]
    print(f"Queue{tmp}:{ans}")
print(*cards)