# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:46:35 2024

@author: Lenovo
"""

while True:
    try:
        s=input().replace("V"," True ").replace("F"," False ").replace("&"," and ").replace("|"," or ").replace("!"," not ")
        flag=eval(s)
        print("V" if flag else "F")
    except EOFError:
        break