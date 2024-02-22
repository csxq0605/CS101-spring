# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:18:44 2024

@author: Lenovo
"""

r1=r2=i=0
def dfs(d1,d2):
    global r1,r2,i
    r1=max(r1,d1)
    r2=max(r2,d2)
    cnt=1
    while s[i]:
        if s[i]=='d':
            i+=1
            dfs(d1+1,d2+cnt)
            cnt+=1
        else:
            i+=1
            return

s=list(input())+[""]
r1=r2=-1
i=0
dfs(0,0)
print(f"{r1} => {r2}")