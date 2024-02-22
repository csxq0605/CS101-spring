# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:09:55 2024

@author: Lenovo
"""

n,m=map(int,input().split())
line=[True]*n
num,i,j=0,0,0
while num<n-1:
    if line[j%n]==True:
        i+=1
    if i==m:
        line[j%n]=False
        i=0
        num+=1
        print(j%n+1,end=" ")
    j+=1