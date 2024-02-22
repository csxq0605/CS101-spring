# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:44:57 2024

@author: Lenovo
"""

ans=0
def code(pos,n):
    global ans
    if n==4 and pos==len(s):
        ans+=1
    elif n>=4:
        return
    for i in range(1,4):
        if pos+i>len(s):
            break
        num=s[pos:pos+i]
        if check(num):
            code(pos+i,n+1)
        else:
            break

def check(num):
    if 0<=int(num)<=500 and (len(num)==1 or (len(num)>=2 and num[0]!="0")):
        return True
    else:
        return False

s=input()
ans=0
code(0,0)
print(ans)