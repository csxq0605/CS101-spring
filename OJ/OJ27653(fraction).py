# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:55:34 2024

@author: Lenovo
"""

from math import gcd
class fraction:
    def __init__(self,zi,mu):
        self.zi=zi
        self.mu=mu
    def __add__(self,other):
        zi=self.zi*other.mu+self.mu*other.zi
        mu=self.mu*other.mu
        m=gcd(zi,mu)
        zi//=m
        mu//=m
        return str(zi)+"/"+str(mu)
    
l=list(map(int,input().split()))
a,b=fraction(l[0],l[1]),fraction(l[2],l[3])
print(a+b)