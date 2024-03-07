# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:56:07 2024

@author: Lenovo
"""

import math
for _ in range(int(input())):
    n=int(input())
    ans=(n+1)*n//2
    m=int(math.log(n,2))
    ans-=2*(2**(m+1)-1)
    print(ans)