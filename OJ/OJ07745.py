# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:34:41 2024

@author: Lenovo
"""

l=list(map(int,input().split()))
odd,even=[],[]
for num in l:
    if num%2:
        odd.append(num)
    else:
        even.append(num)
l=sorted(odd,reverse=True)+sorted(even)
print(*l)