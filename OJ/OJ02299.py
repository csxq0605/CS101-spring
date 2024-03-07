# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:35:24 2024

@author: Lenovo
"""

def merge(l,m,r):
    left=speeds[l:m+1]
    right=speeds[m+1:r+1]
    inv_count=0
    i=j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]>=right[j]:
            speeds[k]=left[i]
            i+=1
        else:
            inv_count+=len(left)-i
            speeds[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        speeds[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        speeds[k]=right[j]
        j+=1
        k+=1
    return inv_count

def count(l,r):
    inv_count=0
    if l<r:
        m=(l+r)//2
        inv_count+=count(l,m)
        inv_count+=count(m+1,r)
        inv_count+=merge(l,m,r)
    return inv_count

while True:
    n=int(input())
    if n==0:
        break
    speeds=[0]*n
    for i in range(n-1,-1,-1):
        speeds[i]=int(input())
    result=count(0,n-1)
    print(result)