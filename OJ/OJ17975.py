# -*- coding: utf-8 -*-
"""
Created on Fri May 10 23:44:43 2024

@author: Lenovo
"""

from math import sqrt
import sys
input = sys.stdin.read
l = input().split()
ind = 0
N = int(l[ind])
ind += 1
M = int(l[ind])
ind += 1
keys = [int(i) for i in l[ind:ind + N]]
table = [None] * M
positions = []
offset=[0]
for i in range(1 ,int(sqrt(M)) + 2):
    offset.append(i**2)
    offset.append(-i**2)
for key in keys:
    pos = key % M
    for off in offset:
        if table[(pos + off) % M] is None:
            pos = (pos + off) % M
            break
        elif table[(pos + off) % M] == key:
            pos = (pos + off) % M
            break
    table[pos] = key
    positions.append(str(pos))
print(' '.join(positions))