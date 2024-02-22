# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by ==苏王捷 工学院==



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows 11

Python编程环境：Spyder IDE 5.5.0



## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：简单递推公式dp



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 00:24:25 2024

@author: Lenovo
"""

n=int(input())
dp=[0]*(n+1)
dp[1]=dp[2]=1
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
print(dp[-1])

```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-02-19 131019](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-02-19 131019.png)



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：按顺序一个个找



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:21:51 2023
 
@author: Lenovo
"""
 
 
word=[c for c in input().lower()]
letters=["h","e","l","l","o"]
s=""
j=0
for i in range(len(word)):
    if word[i]==letters[0]:
        s+=word[i]
        letters.remove(letters[0])
        j+=1
    if j==5:
        break
if s=="hello":
    print("YES")
else:
    print("NO")
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-02-19 130949](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-02-19 130949.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：逐一扫描排查改变



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:39:31 2023
 
@author: Lenovo
"""
 
word=input().lower()
list=[]
vowels=["a","e","i","o","u","y"]
word1=""
for i in range(len(word)):
    list.append(word[i])
for i in range(len(list)):
    if list[i] not in vowels:
        word1+="."+list[i]
print(word1)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-02-19 130957](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-02-19 130957.png)



### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：欧拉筛法打出质数表，逐一寻找



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:21:46 2024

@author: Lenovo
"""

from math import sqrt
n=10000
ls,x,y=[True]*(n+1),2,int(sqrt(n))+1
while x<y:
    if ls[x]==True:
        for i in range(x*2,n+1,x):
            ls[i]=False
    x+=1
ls=set([i for i in range(2,n+1) if ls[i]==True])

n=int(input())
for i in ls:
    if (n-i) in ls:
        print(i,n-i)
        break

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-02-19 131040](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-02-19 131040.png)



### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：用+分割，找到最大的次方项



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:24:32 2023

@author: Lenovo
"""

string=list(input().split("+"))
ans=0
for i in string:
    if i.find("n")!=-1:
        index=i.find("n")
        try:
            num1=int(i[0:index])
        except:
            num1=1
        num2=int(i[index+2:])
        if num1!=0:
            ans=max(num2,ans)
print(f"n^{ans}")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-02-19 131055](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-02-19 131055.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：找到票数最多的群体，按序输出



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 00:26:29 2024

@author: Lenovo
"""

from collections import Counter
l=list(map(int,input().split()))
count=Counter(l)
maxn=max(list(count.values()))
ans=[]
for i in count.keys():
    if count[i]==maxn:
        ans.append(i)
ans.sort()
print(*ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-02-19 131113](C:\Users\Lenovo\Pictures\Screenshots\屏幕截图 2024-02-19 131113.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“数算pre每日选做”、CF、LeetCode、洛谷等网站题目。==

练习完了，以后的作业题是不是也是做过的呢？    >.<



