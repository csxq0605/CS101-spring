# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:41:33 2024

@author: Lenovo
"""

def lock_changed(l,i):
    l[i]=(l[i]+1)%2
    if(i-1>=0):
        l[i-1]=(l[i-1]+1)%2
    if(i+1<=len(l)-1):
        l[i+1]=(l[i+1]+1)%2

l1=[int(i) for i in input()]
final=[int(i) for i in input()]
l2=l1.copy()
count=float("inf")
count1=0
for i in range(1,len(l1)):
    if l1[i-1]!=final[i-1]:
        count1+=1
        lock_changed(l1,i)
if l1==final:
    count=count1 
count2=1
lock_changed(l2,0)
for i in range(1,len(l2)):
    if l2[i-1]!=final[i-1]:
        count2+=1
        lock_changed(l2,i)
if l2==final:
    count=min(count,count2)
print(count if count!=float("inf") else "impossible")