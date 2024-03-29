# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:48:38 2024

@author: Lenovo
"""

x=input()
n=len(x)
sx=set(x)
while True:
    try:
        now=input()
        snow=set(now)
        if snow!=sx or len(now)!=n:
            print("NO")
            continue
        stack,vis,cnt=[],set(),0
        for char in x:
            stack.append(char)
            while stack and stack[-1]==now[cnt]:
                cnt+=1
                stack.pop()
        print("NO" if stack else "YES")
    except EOFError:
        break