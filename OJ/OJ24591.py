# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:43:08 2024

@author: Lenovo
"""

n=int(input())
for _ in range(n):
    s=list(input().replace("+"," + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").replace("("," ( ").replace(")"," ) ").split())
    num,action=[],[]
    actions=["+","-","*","/"]
    dic={"(":0,"+":1,"-":1,"*":2,"/":2}
    for char in s:
        if char==")":
            while action and action[-1]!="(":
                num.append(action.pop())
            action.pop()
        elif char=="(":
            action.append(char)
        elif char in actions:
            while action and dic[action[-1]]>=dic[char]:
                num.append(action.pop())
            action.append(char)
        else:
            num.append(char)
    while action:
        num.append(action.pop())
    print(*num)