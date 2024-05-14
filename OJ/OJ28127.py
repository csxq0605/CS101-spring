# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:36:45 2024

@author: Lenovo
"""

m=int(input())
dic={}
for i in range(m):
    team,no,res=input().split(",")
    if team not in dic.keys():
        dic[team]=(set(),0)
    s,num=dic[team]
    if res=="yes":s.add(no)
    dic[team]=(s,num+1)
l=[]
for team in dic.keys():
    num,tot=dic[team]
    l.append([team,len(num),tot])
l.sort(key=lambda x:(-x[1],x[2],x[0]))
for i in range(1,min(len(l)+1,13)):
    print(i,*l[i-1])