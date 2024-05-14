# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:36:14 2024

@author: Lenovo
"""

n,m=map(int,input().split())
dic={}
ans=0
for i in range(n):
    name,v,num=input().split()
    dic[name]=[int(v),int(num)]
    ans+=int(v)*int(num)
for i in range(m):
    a,b,c=input().split()
    dic[a]=[dic[a][0],max(dic[a][1]-1,0)]
    dic[b]=[dic[b][0],max(dic[b][1]-1,0)]
    dic[c]=[dic[c][0],max(dic[c][1]-1,0)]
for l in dic.values():
    ans-=l[0]*l[1]
print(ans)