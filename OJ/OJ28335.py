# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:07:05 2024

@author: Lenovo
"""

while True:
    try:
        s=input()
        dic={chr(i):0 for i in range(97,123)}
        ans=""
        for char in s:
            if char==" ":
                continue
            dic[char]+=1
            if dic[char]==123-ord(char):
                ans+=chr(ord(char)-32)
        if ans:
            print(len(ans),ans)
        else:
            print(0)
    except EOFError:
        break