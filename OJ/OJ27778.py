# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:31:49 2024

@author: Lenovo
"""

import hashlib
def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

T=int(input())
for _ in range(T):
    str1=input()
    str2=input()
    if md5(str1)==md5(str2):
        print("Yes")
    else:
        print("No")