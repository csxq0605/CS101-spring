# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:32:12 2023

@author: Lenovo
"""

def max_subarray_sum(matrix):
    maxval=float('-inf')
    for i in range(n):
        b=[0]*n
        for j in range(i,n):
            for k in range(n):
                b[k]+=matrix[j][k]
            _sum=0
            for num in b:
                if _sum+num>0:
                    _sum+=num
                else:
                    _sum=num
                maxval=max(maxval,_sum)
    return maxval

n=int(input())
l=[]
while True:
    try:
        _input=input()
        if _input=="":
            continue
        else:
            l.extend(list(map(int,_input.split())))
    except EOFError:
        break
martix=[[0]*n for _ in range(n)]
for i in range(n):
    martix[i][0:n]=map(int,l[i*n:(i+1)*n])
result=max_subarray_sum(martix)
print(result)