# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:58:56 2024

@author: Lenovo
"""

def check(n,out):
    stack=[0]*1000
    po=0
    top=0
    for i in range(1,n+1):
        for j in range(po+1,out[i]+1):
            po=j
            stack[top]=j
            top+=1
        if stack[top-1]!=out[i]:
            return 0
        top-=1
    return 1

x=input()
n=len(x)
dic={x[i-1]:i for i in range(1,n+1)}
while True:
    try:
        now=input()
        if len(now)!=n:
            print("NO")
            continue
        out=[0]
        vis=set()
        flag=1
        for i in now:
            if i in vis:
                print("NO")
                flag=0
                break
            out+=[dic[i]]
            vis.add(i)
        if not flag:
            continue
        print("YES" if check(n,out) else "NO")
    except KeyError:
        print("NO")
    except EOFError:
        break