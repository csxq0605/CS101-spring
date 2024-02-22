# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:18:39 2024

@author: Lenovo
"""

n=int(input())
matrix=[[0]*(2*n-1) for i in range(2*n-1)]
x,y=0,n-1
for i in range(1,(2*n-1)**2+1):
    matrix[x][y]=i
    if (x==0 and y==2*n-2) or (x!=0 and y!=2*n-2 and matrix[x-1][y+1]!=0):
        x+=1
    elif x==0:
        x=2*n-2
        y+=1
    elif y==2*n-2:
        x-=1
        y=0
    else:
        x-=1
        y+=1
for row in matrix:
    print(*row)