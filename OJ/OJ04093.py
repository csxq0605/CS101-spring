# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 00:27:25 2024

@author: Lenovo
"""

n=int(input())
dic={i:set() for i in range(n)}
for i in range(n):
    dic[i].update(map(int,input().split()[1:]))
m=int(input())
for i in range(m):
    ans,flag=set(),False
    l=input().split()
    for id,tf in enumerate(l):
        if tf=="1":
            ans=ans.intersection(dic[id]) if flag else dic[id]
            flag=True
    for id,tf in enumerate(l):    
        if tf=="-1" and ans:
            ans=set([Id for Id in ans if Id not in dic[id]])
    if not ans:
        print("NOT FOUND")
    else:
        ans=sorted(ans)
        print(*ans)

    
n=int(input())
dic={i:0 for i in range(n)}
maxn=0
for i in range(n):
    l=list(map(int,input().split()))
    for num in set(l[1::]):
        maxn=max(num,maxn)
        dic[i]+=1<<num
m=int(input())
for i in range(m):
    ans=(1<<maxn+1)-1
    l=input().split()
    for id,tf in enumerate(l):
        if tf=="1":
            ans=ans&dic[id]
        elif tf=="-1":
            ans=ans&~dic[id]
    if not ans:
        print("NOT FOUND")
    else:
        res=[i for i in range(maxn+1) if (1<<i)&ans]
        print(*res)
  
        
n=int(input())
Word=[set() for _ in range(n)]
for i in range(n):
    values=list(map(int,input().split()))
    m, values=values[0],values[1:]
    Word[i].update(values)
m=int(input())
for _ in range(m):
    tag=list(map(int,input().split()))
    result=set()
    for i in range(n):
        if tag[i]!=1:
            continue
        if not result:
            result=set(Word[i])
            continue
        result&=Word[i]
        if not result:
            break
    for i in range(n):
        if tag[i]!=-1:
            continue
        result-=Word[i]
    if not result:
        print("NOT FOUND")
    else:
        print(*sorted(result))