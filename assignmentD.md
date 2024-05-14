# Assignment #D: May月考

Updated 1654 GMT+8 May 8, 2024

2024 spring, Complied by ==苏王捷 221000000000020工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：Spyder IDE 5.5.3



## 1. 题目

### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：EASY



代码

```python
# 
tree,n=map(int,input().split())
line=[]
for i in range(n): 
    line.append([int(i) for i in input().split()])
road=[1]*(tree+1)
for i in range(n):
    for j in range(line[i][0]-1,line[i][1]):
        road[j]=0
print(sum(road))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240508223709513](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240508223709513.png)



### 20449: 是否被5整除

http://cs101.openjudge.cn/practice/20449/



思路：手动计算二进制数



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:26:33 2024

@author: Lenovo
"""

a=input()
ans=""
num=0
for i in range(len(a)):
    num=num*2+int(a[i])
    ans+=str(int(num%5==0))
print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240508223826807](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240508223826807.png)



### 01258: Agri-Net

http://cs101.openjudge.cn/practice/01258/



思路：Prim，并查集



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:09:37 2024

@author: Lenovo
"""

class Edge:
    def __init__(self,s,e,w):
        self.s=s
        self.e=e
        self.w=w
    def __lt__(self,other):
        return self.w<other.w
        
class DisjSet:
    def __init__(self,n):
        self.p=[i for i in range(n)]
        
    def find(self,x):
        if x!=self.p[x]:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    
    def merge(self,x,y):
        xroot,yroot=self.find(x),self.find(y)
        if xroot!=yroot:
            self.p[yroot]=xroot

while True:
    try:
        n=int(input())
        matrix=[list(map(int,input().split())) for i in range(n)]
        l=[]
        for i in range(n):
            for j in range(n):
                l.append(Edge(i,j,matrix[i][j]))
        l.sort()
        s=DisjSet(n)
        ans=cnt=0
        for edge in l:
            if s.find(edge.s)!=s.find(edge.e):
                ans+=edge.w
                s.merge(edge.s,edge.e)
                cnt+=1
            if cnt==n-1:
                break
        print(ans)
    except EOFError:
        break

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240508223905759](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240508223905759.png)



### 27635: 判断无向图是否连通有无回路(同23163)

http://cs101.openjudge.cn/practice/27635/



思路：用bfs找联通和dfs找回路



代码

```python
# from collections import deque
def dfs(x,p):
    for i in dic[x]:
        if i not in vis:
            vis.add(i)
            if dfs(i,x):
                return True
        elif i!=p:
            return True
    return False

n,m=map(int,input().split())
dic={i:[] for i in range(n)}
for i in range(m):
    a,b=map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
vis=set()
q=deque()
vis.add(0)
q.append(0)
while q:
    node=q.popleft()
    for i in dic[node]:
        if i not in vis:
            vis.add(i)
            q.append(i)
print("connected:yes" if len(vis)==n else "connected:no")
vis=set()
flag=False
for i in range(n):
    if i not in vis:
        vis.add(i)
        flag=dfs(i,-1)
        if flag:
            break
print("loop:yes" if flag else "loop:no")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240508224020242](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240508224020242.png)





### 27947: 动态中位数

http://cs101.openjudge.cn/practice/27947/



思路：考试硬卡我十分钟，一个小顶堆和一个大顶堆存储两边数字



代码

```python
# 
from heapq import heappush,heappop
t=int(input())
for _ in range(t):
    l=[0]+list(map(int,input().split()))
    m=len(l)-1
    ans=[l[1]]
    h1,h2=[],[]
    num=l[1]
    for i in range(2,m+1):
        if l[i]<=num:
            heappush(h1,-l[i])
        else:
            heappush(h2,l[i])
        if i%2:
            if len(h1)==len(h2):
                ans.append(num)
            elif len(h1)>len(h2):
                heappush(h2,num)
                num=-heappop(h1)
                ans.append(num)
            else:
                heappush(h1,-num)
                num=heappop(h2)
                ans.append(num)
    print(len(ans))
    print(*ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240508224134598](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240508224134598.png)



### 28190: 奶牛排队

http://cs101.openjudge.cn/practice/28190/



思路：考试就差一分钟！！！！！！！

数据太弱，暴力O(N^3)也能过

也可单调栈



代码

```python
# 
n=int(input())
h=[0]+[int(input()) for i in range(n)]
ans=0
for i in range(n,1,-1):
    for j in range(i-1,0,-1):
        if h[i]<=h[j]:break
        flag=True
        for k in range(j+1,i):
            if h[k]>=h[i] or h[k]<=h[j]:
                flag=False
                break
        if flag:
            ans=max(ans,i-j+1)
            if ans==n:
                break
if ans==1:
    ans=0
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240508224245908](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240508224245908.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

玛雅，史上第一次AC5

鉴定为被T1卡了+对T2的OJ数据太不自信

不过T2的单调栈确实没想出来



