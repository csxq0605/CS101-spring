# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:33:31 2024

@author: Lenovo
"""

def find(stu):
    if pre[stu]==stu:
        return stu
    return find(pre[stu])

def join(stu1,stu2):
    root1,root2=find(stu1),find(stu2)
    if root1!=root2:
        pre[root2]=root1

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    pre=[i for i in range(n)]
    for _ in range(m):
        l=list(map(int,input().split()))
        num,l=l[0],l[1:]
        for i in range(num):
            if i==0:
                prestu=l[i]
            join(prestu,l[i])
            prestu=l[i]
    ans=1
    for i in range(1,n):
        if find(0)==find(i):
            ans+=1
    print(ans)