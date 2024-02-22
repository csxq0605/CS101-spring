# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:25:18 2023

@author: Lenovo
"""

def dpHappi():
    happi=[0]*45
    for day in range(45):
        for x in [x for x in List if x[1]<=day]:
            si,ei,vi=map(int,x)
            if day==0:
                happi[day]=max(vi,happi[day])
            elif si>0:
                happi[day]=max(happi[day-1],happi[si-1]+vi,happi[day])
            else:
                happi[day]=max(vi,happi[day],happi[day-1])
    return happi[-1]
 
n=int(input())
dic={"1.7":0,"1.8":1,"1.9":2,"1.10":3,"1.11":4,"1.12":5,"1.13":6,"1.14":7,"1.15":8,"1.16":9,"1.17":10,"1.18":11,"1.19":12,"1.20":13,"1.21":14,"1.22":15,"1.23":16,"1.24":17,"1.25":18,"1.26":19,"1.27":20,"1.28":21,"1.29":22,"1.30":23,"1.31":24,"2.1":25,"2.2":26,"2.3":27,"2.4":28,"2.5":29,"2.6":30,"2.7":31,"2.8":32,"2.9":33,"2.10":34,"2.11":35,"2.12":36,"2.13":37,"2.14":38,"2.15":39,"2.16":40,"2.17":41,"2.18":42,"2.19":43,"2.20":44}
List=[]
for i in range (n):
    s,e,v=input().split()
    si=dic[s]
    try:
        ei=dic[e]
    except KeyError:
        continue
    vi=int(v)
    List.append([si,ei,vi])
print(dpHappi())