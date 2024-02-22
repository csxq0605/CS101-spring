# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:26:33 2024

@author: Lenovo
"""

a=input()
ans=""
num=0
for i in range(len(a)):
    num=num*2+int(a[i])
    ans+=str(int(num%5==0))
print(ans)