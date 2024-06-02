# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:14:17 2024

@author: Lenovo
"""

t=int(input())
for _ in range(t):
    f=input()
    if f=="encrypt":
        s=input()
        stack=[]
        ans=""
        for char in s:
            stack.append(char)
            if (ord(char)-96)%2==0:
                while stack:
                    ans+=stack.pop()
        if stack:
            ans+="0"
            while stack:
                ans+=stack.pop()
    else:
        s=input()
        stack=[]
        ans=""
        for char in s:
            if char=="0" or (ord(char)-96)%2==0:
                while stack:
                    ans+=stack.pop()
            if char=="0":
                continue
            stack.append(char)
        if stack:
            while stack:
                ans+=stack.pop()
    print(ans)