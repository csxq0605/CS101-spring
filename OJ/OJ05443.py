# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:35:01 2024

@author: Lenovo
"""

minlen,totallen,ans=float("inf"),0,[]
def dfs(s,t):
    global totallen,minlen,ans
    if s==t:
        if totallen<minlen:
            ans=tmp.copy()
        return
    for road in citymap[s]:
        d,l=road['d'],road['l']
        if d in visited:
            continue
        length=l+totallen
        if length>=minlen or length>=minl[d]:
            continue
        totallen=length
        minl[d]=length
        visited.add(d)
        tmp.append("("+str(l)+")")
        tmp.append(d)
        dfs(d,t)
        totallen-=l
        visited.discard(d)
        tmp.pop()
        tmp.pop()

p=int(input())
destinations=[input() for _ in range(p)]
q=int(input())
citymap={i:[] for i in destinations}
for i in range(q):
    s,d,l=map(str,input().split())
    citymap[s].append({"d":d,"l":int(l)})
    citymap[d].append({"d":s,"l":int(l)})
r=int(input())
for _ in range(r):
    s,t=input().split()
    minl={i:float("inf") for i in destinations}
    minlen,totallen,ans,tmp=float("inf"),0,[],[s]
    visited=set()
    visited.add(s)
    dfs(s,t)
    print("->".join(ans))