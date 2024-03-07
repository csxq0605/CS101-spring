# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:06:49 2024

@author: Lenovo
"""

while True:
    try:
        n=input()
        flag=True
        stack=[]
        for num in n:
            stack.append(num)
        for num in n:
            flag=flag and stack.pop()==num
        print("YES" if flag else "NO")
    except EOFError:
        break