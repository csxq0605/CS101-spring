# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by ==苏王捷 工学院==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：Spyder IDE 5.5.0



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/2024sp_routine/27653/



思路：重载加法运算符



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:55:34 2024

@author: Lenovo
"""

from math import gcd
class fraction:
    def __init__(self,zi,mu):
        self.zi=zi
        self.mu=mu
    def __add__(self,other):
        zi=self.zi*other.mu+self.mu*other.zi
        mu=self.mu*other.mu
        m=gcd(zi,mu)
        zi//=m
        mu//=m
        return str(zi)+"/"+str(mu)
    
l=list(map(int,input().split()))
a,b=fraction(l[0],l[1]),fraction(l[2],l[3])
print(a+b)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240224110123521](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240224110123521.png)



### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：用相对价值高的物品先填



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:58:15 2023

@author: Lenovo
"""

class metal:
    def __init__(self,v,n,contraryvalue):
        self.n=n
        self.v=v
        self.contraryvalue=contraryvalue

n,w=map(int,input().split())
value=0
metals=[]
for i in range(n):
    l=[int(i) for i in input().split()]
    metals.append(metal(l[0],l[1],l[0]/l[1]))
metals.sort(key=lambda x:x.contraryvalue)
while w>0 and metals:
    metal_i=metals.pop()
    if w>=metal_i.n:
        value+=metal_i.v
        w-=metal_i.n
    else:
        value+=metal_i.contraryvalue*w
        w=0
print("%.1f" % value)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240224110232923](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240224110232923.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：用伤害高的技能先打



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:43:00 2023

@author: Lenovo
"""

ncases=int(input())
for _ in range(ncases):
    n,m,b=map(int,input().split())
    l,initial=[],m
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:(x[0],-x[1]))
    t=0
    for i in range(len(l)):
        if t!=l[i][0]:
            t=l[i][0]
            m=initial
        if m>0 and b>0:
            b-=l[i][1]
            m-=1
        if b<=0:
            print(t)
            break
    if b>0:
        print("alive")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240224110324102](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240224110324102.png)



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：打出t-primes表，判断



##### 代码

```python
n=1000000
ls,x,l=[True]*n,2,set()
for x in range(2,n):
    if ls[x]==True:
        l.add(x**2)
        for i in range(x**2,n,x):
            ls[i]=False
input()
for i in map(int,input().split()):
    print(["NO","YES"][i in l])

```



代码运行截图 ==![image-20240224110703113](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240224110703113.png)（AC代码截图，至少包含有"Accepted")==





### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：取余数计算从头或从尾去除最少几个数后变成非整除和



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:25:09 2023
 
@author: Lenovo
"""
 
n=int(input())
for i in range(n):
    l,x=map(int,input().split())
    line=[int(i)%x for i in input().split()]
    if set(line)=={0}:
        print(-1)
    elif sum(line)%x==0:
        for j in range(l):
            if line[j]!=0:
                head=j+1
                break
        for j in range(l-1,-1,-1):
            if line[j]!=0:
                back=l-j
                break
        print(l-min(head,back))
    else:
        print(l)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240224110858291](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240224110858291.png)



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：打出t-primes表，逐个寻找



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:07:58 2023

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
ls=set([i**2 for i in range(2,n+1) if ls[i]==True])

m,n=map(int,input().split())
for _ in range(m):
    scores=list(map(int,input().split()))
    score=0
    for i in scores:
        if i in ls:
            score+=i
    print("%.2f"%(score/len(scores)) if score else 0)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240224110451490](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240224110451490.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

灰常简单的题目，让我能直接交作业

感觉和xk转院考一样的难度（？）



