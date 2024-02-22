# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:26:57 2024

@author: Lenovo
"""

n=int(input())
enc=input()
l=len(enc)
matrix=[[0]*n for i in range(l//n)]
flag,line=1,0
for i in range(0,l,n):
    if flag:
        matrix[line]=list(enc[i:i+n])
        flag=0
    else:
        matrix[line]=list(enc[i:i+n])[::-1]
        flag=1
    line+=1
for i in range(n):
    for j in range(l//n):
        print(matrix[j][i],end="")