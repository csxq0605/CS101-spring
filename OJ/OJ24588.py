# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:43:00 2024

@author: Lenovo
"""

n=int(input())
for _ in range(n):
    l=list(input().split())
    stack=[]
    for char in l:
        if char=="+":
            a,b=stack.pop(),stack.pop()
            stack.append(a+b)
        elif char=="-":
            a,b=stack.pop(),stack.pop()
            stack.append(b-a)
        elif char=="*":
            a,b=stack.pop(),stack.pop()
            stack.append(a*b)
        elif char=="/":
            a,b=stack.pop(),stack.pop()
            stack.append(b/a)
        else:
            stack.append(float(char))
    ans=stack.pop()
    print("%.2f"% ans)