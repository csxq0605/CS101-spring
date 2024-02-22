# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:33:03 2024

@author: Lenovo
"""

from math import log2,log,sqrt
def f(x):
    return x**2+x+1+log2(x)-y

def f1(x):
    return 2*x+1+1/(x*log(2))

while True:
    try:
        y=int(input())
        x0=sqrt(y-1)
        while abs(f(x0))>1e-3:
            x0=x0-f(x0)/f1(x0)
        print(round(x0,4))
    except EOFError:
        break