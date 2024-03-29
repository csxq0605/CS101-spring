# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:36:55 2024

@author: Lenovo
"""

def Print(num):
    for i in range(num):
        print("|     ",end="")
        
def build(level,flag):
    files=[]
    if flag:
        if flag[0]=="d":
            Print(level)
            print(flag)
            build(level+1,"")
        else:
            files.append(f)
    while True:
        s=input()
        if s[0]=="d":
            Print(level)
            print(s)
            build(level+1,"")
        elif s[0]=="f":
            files.append(s)
        elif s=="]":
            for file in sorted(files):
                Print(level-1)
                print(file)
            return
        else:
            for file in sorted(files):
                print(file)
            return

n=1
while True:
   f=input()
   if f=="#":
       break
   print(f"DATA SET {n}:")
   print("ROOT")
   build(1,f)
   print()
   n+=1