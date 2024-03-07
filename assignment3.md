# Assignment #3: March月考

Updated 1537 GMT+8 March 6, 2024

2024 spring, Complied by ==苏王捷 工学院==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows11 23H2

Python编程环境：Spyder IDE 5.5.0



## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/



思路：最长递减子序列



##### 代码

```python
# 
k=int(input())
l=list(map(int,input().split()))
dp=[0]*k
for i in range(k-1,-1,-1):
    maxn=1
    for j in range(k-1,i,-1):
        if l[i]>=l[j] and dp[j]+1>maxn:
            maxn=dp[j]+1
    dp[i]=maxn
print(max(dp))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240306171911606](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240306171911606.png)



**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147



思路：递归移动盘子



##### 代码

```python
# 
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:12:15 2024

@author: Lenovo
"""

def hanoitower(n,fro,mid,to,No):
    if n==1:
        print(f"{No}:{fro}->{to}")
        return
    hanoitower(n-1,fro,to,mid,No)
    print(f"{No+n-1}:{fro}->{to}")
    hanoitower(n-1,mid,fro,to,No)

n,a,b,c=input().split()
n=int(n)
hanoitower(n,a,b,c,1)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240306171952855](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240306171952855.png)



**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253



思路：用双端队列又实现了一次，本质上就是成环



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:24:33 2024

@author: Lenovo
"""

from collections import deque
while True:
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:
        break
    stack=[]
    q=deque([str(i) for i in range(p,n+1)]+[str(i) for i in range(1,p)])
    count=0
    while q:
        num=q.popleft()
        count+=1
        if count==m:
            stack.append(num)
            count=0
        else:
            q.append(num)
    print(",".join(stack))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306172048240](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240306172048240.png)



**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554



思路：贪心，时间短的先做实验



##### 代码

```python
# 
n=int(input())
l=list(map(int,input().split()))
line=[]
for i in range(1,n+1):
    line.append([l[i-1],i])
line.sort()
ans=0
for i in range(n):
    print(line[i][1],end=" ")
    ans+=line[i][0]*(n-1-i)
print()
print("%.2f"%(ans/n))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306172125473](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240306172125473.png)



**19963:买学区房**

http://cs101.openjudge.cn/practice/19963



思路：算出两个中位数然后找出个数



##### 代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:28:30 2023

@author: Lenovo
"""

n=int(input())
pairs=[i[1:-1] for i in input().split()]
distances=[sum(map(int,i.split(','))) for i in pairs]
prices=list(map(int,input().split()))
values=[distances[i]/prices[i] for i in range(n)]
pnew=sorted(prices)
vnew=sorted(values)
if n%2==0:
    pmid=(pnew[n//2]+pnew[n//2-1])/2
    vmid=(vnew[n//2]+vnew[n//2-1])/2
else:
    pmid=pnew[n//2]
    vmid=vnew[n//2]
ans=0
for i in range(n):
    if values[i]>vmid and prices[i]<pmid:
        ans+=1
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306172208428](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240306172208428.png)



**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300



思路：用字典存数据，对每个排序输出



##### 代码

```python
# 
from collections import defaultdict
n=int(input())
dic=defaultdict(list)
for i in range(n):
    t,w=input().split("-")
    dic[t].append(w)
l=sorted(dic.items())
for i in range(len(l)):
    t,w=l[i]
    wsort=[[float(w[x][:-1])*1000 if w[x][-1]=="B" else float(w[x][:-1]),x] for x in range(len(w))]
    wsort.sort()
    wnew=[w[wsort[x][1]] for x in range(len(w))]
    l[i]=[t,wnew]
for i in range(len(l)):
    print(f"{l[i][0]}:",", ".join(l[i][1]))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240306172252069](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240306172252069.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

10分钟光速AC，全是老题老代码

警觉之前有两题还是C++实现于是重写了Python的代码

剩下的又重写检验了一下语法糖的进步水平 >.<



