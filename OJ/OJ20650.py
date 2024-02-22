# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:07:20 2024

@author: Lenovo
"""

text1,text2=input(),input()
l1,l2=len(text1),len(text2)
dp=[[0]*(l2+1) for i in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if text1[i-1]==text2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[l1][l2])