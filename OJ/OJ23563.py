# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:25:39 2024

@author: Lenovo
"""

string=list(input().split("+"))
ans=0
for i in string:
    if i.find("n")!=-1:
        index=i.find("n")
        try:
            num1=int(i[0:index])
        except:
            num1=1
        num2=int(i[index+2:])
        if num1!=0:
            ans=max(num2,ans)
print(f"n^{ans}")