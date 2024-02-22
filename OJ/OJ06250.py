# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:06:37 2024

@author: Lenovo
"""

s,s1,s2=input().split(",")
if len(s)<len(s1) or len(s)<len(s2):
    print(-1)
    quit()
index1=s.find(s1)
index2=-1
for i in range(len(s)-len(s2)+1):
    if s[i]==s2[0]:
        flag=True
        for j in range(1,len(s2)):
            if s[i+j]!=s2[j]:
                flag=False
                break
        if flag:
            index2=max(i,index2)
if index1!=-1 and index2!=-1 and index1+len(s1)-1<index2:
    print(index2-(index1+len(s1)-1)-1)
else:
    print(-1)