# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:12:39 2024

@author: Lenovo
"""

def get_ud(i,j):
    return (2*n+1)*(i-1)+j-1

def get_lr(i,j):
    return (2*n+1)*(i-1)+j+n-1

def build():
    global cnt
    cnt=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            base[i][j]=0
            base[i][j]|=bit[get_ud(i,j)]|bit[get_ud(i+1,j)]
            base[i][j]|=bit[get_lr(i,j)]|bit[get_lr(i,j+1)]
            cnt+=1
            squ[cnt]=base[i][j]
    for siz in range(2,n+1):
        for i in range(1,n-siz+2):
            for j in range(1,n-siz+2):
                cnt+=1
                squ[cnt]=0
                for w in range(siz):
                    for h in range(siz):
                        squ[cnt]^=base[i+w][j+h]

def dfs(d,state):
    if d==maxd:
        for i in range(1,cnt+1):
            if squ[i]&state==squ[i]:
                return False
        return True
    s=state
    need=0
    del_val=0
    for i in range(1,cnt+1):
        if squ[i]&s==squ[i]:
            need+=1
            s^=squ[i]
            if not del_val:
                del_val=squ[i]
    if d+need>maxd:
        return False
    for i in range(1,tot+1):
        if del_val&bit[i-1]==bit[i-1]:
            if dfs(d+1,state^bit[i-1]):
                return True
    return False

T=int(input())
bit= [1<<i for i in range(61)]
for _ in range(T):
    n=int(input())
    tot=2*n*(n+1)
    state=bit[tot]-1
    l=list(map(int,input().split()))
    m=l[0]
    m_values=l[1:]
    for x in m_values:
        state^=bit[x-1]
    base=[[0]*(n+1) for _ in range(n+1)]
    squ=[0]*56
    build()
    maxd=0
    while True:
        if dfs(0,state):
            break
        maxd+=1
    print(maxd)