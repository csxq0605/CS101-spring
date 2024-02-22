# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:51:54 2024

@author: Lenovo
"""

s=input()
stack=[]
for _ in s:
    if _==")":
        temp=[]
        while stack and stack[-1]!="(":
            temp.append(stack.pop())
        if stack:
            stack.pop()
        stack.extend(temp)
    else:
        stack.append(_)
print("".join(stack))