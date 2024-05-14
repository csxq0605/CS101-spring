# Assignment #9: 图论：遍历，及 树算

Updated 1739 GMT+8 Apr 14, 2024

2024 spring, Complied by ==苏王捷 工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：Spyder IDE 5.5.3



## 1. 题目

### 04081: 树的转换

http://cs101.openjudge.cn/dsapre/04081/



思路：dfs找距离



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:18:44 2024

@author: Lenovo
"""

r1=r2=i=0
def dfs(d1,d2):
    global r1,r2,i
    r1=max(r1,d1)
    r2=max(r2,d2)
    cnt=1
    while s[i]:
        if s[i]=='d':
            i+=1
            dfs(d1+1,d2+cnt)
            cnt+=1
        else:
            i+=1
            return

s=list(input())+[""]
r1=r2=-1
i=0
dfs(0,0)
print(f"{r1} => {r2}")

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240415194249015](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240415194249015.png)



### 08581: 扩展二叉树

http://cs101.openjudge.cn/dsapre/08581/



思路：建树递归



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:35:56 2024

@author: Lenovo
"""

class Node:
    def __init__(self):
        self.value=None
        self.lchild=None
        self.rchild=None

def build():
    node=Node()
    node.value=l.pop(0)
    return node
    
def Tree(root):
    if root.value==".":
        return
    root.lchild=build()
    Tree(root.lchild)
    root.rchild=build()
    Tree(root.rchild)
    
def midorder(tree):
    if tree.value==".":
        return
    midorder(tree.lchild)
    print(tree.value,end="")
    midorder(tree.rchild)

def lastorder(tree):
    if tree.value==".":
        return
    lastorder(tree.lchild)
    lastorder(tree.rchild)
    print(tree.value,end="")
    
l=list(input())
tree=build()
Tree(tree)
midorder(tree)
print()
lastorder(tree)
print()

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240415194337179](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240415194337179.png)



### 22067: 快速堆猪

http://cs101.openjudge.cn/practice/22067/



思路：堆实现，懒删除



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:26:47 2024

@author: Lenovo
"""

import heapq
from collections import defaultdict
heap,stack,count=[],[],defaultdict(int)
while True:
    try:
        function=list(input().split())
        if function[0]=="pop":
            if stack:
                count[stack.pop()]-=1
        elif function[0]=="push":
            stack.append(int(function[1]))
            count[int(function[1])]+=1
            heapq.heappush(heap,int(function[1]))
        else:
            if stack:    
                while heap and not count[heap[0]]:
                    heapq.heappop(heap)  
                print(heap[0])
    except EOFError:
        break

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240415194445372](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240415194445372.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123



思路：dfs 记录路径数



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:32:15 2023

@author: Lenovo
"""

d=[(1,2),(2,1),(-1,2),(-2,1),(-1,-2),(-2,-1),(1,-2),(2,-1)]
maze=[[0]*11 for _ in range(11)]
ans=0
def dfs(step,x,y):
    global ans,maze
    if step==n*m:
        ans+=1
        return
    for i in range(8):
        nx,ny=d[i]
        nx,ny=x+nx,y+ny
        if 0<=nx<n and 0<=ny<m and not maze[nx][ny]:    
            maze[nx][ny]=1
            dfs(step+1,nx,ny)
            maze[nx][ny]=0

t=int(input())
for i in range(t):
    n,m,x0,y0=map(int,input().split())
    maze=[[0]*11 for _ in range(11)]
    ans=0
    maze[x0][y0]=1
    dfs(1,x0,y0)
    print(ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240415194553810](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240415194553810.png)



### 28046: 词梯

bfs, http://cs101.openjudge.cn/practice/28046/



思路：建词桶 bfs同时记录路径



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:00:19 2024

@author: Lenovo
"""

import heapq
n=int(input())
word,words={},{}
for i in range(n):
    w=input()
    for p in range(4):
        ws=w[:p]+"_"+w[p+1:]
        word[w]=word.get(w,[])+[ws]
        words[ws]=words.get(ws,[])+[w]
start,end=input().split()
vis=set([start])
heap=[]
flag=False
heapq.heappush(heap,(1,[start]))
while heap:
    l,path=heapq.heappop(heap)
    node=path[-1]
    if node==end:
        flag=True
        break
    for ws in word[node]:
        if ws in vis:
            continue
        vis.add(ws)
        for w in words[ws]:
            if w in vis:
                continue
            vis.add(w)
            heapq.heappush(heap,(l+1,path+[w]))
if flag:            
    print(*path)
else:
    print("NO")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240415194656917](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240415194656917.png)



### 28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/



思路：Warnsdorff算法优化，每次走之后可能性最少的地方



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:23:41 2024

@author: Lenovo
"""

move=[(-2, -1),(-2, 1),(-1, -2),(-1, 2),(1, -2),(1, 2),(2, -1),(2, 1)]
def is_valid(x,y):
    return 1<=x<=n and 1<=y<=n and not visited[x][y]

def get_degree(x,y):
    count=0
    for i in range(8):
        dx,dy=x+move[i][0],y+move[i][1]
        if is_valid(dx,dy):
            count+=1
    return count

def dfs(x,y,step):
    if step==n*n:
        return True
    mindind,mind=-1,9
    for i in range(8):
        dx,dy=x+move[i][0],y+move[i][1]
        if is_valid(dx,dy) and get_degree(dx,dy)<mind:
            mindind=i
            mind=get_degree(dx,dy)
    if mindind!=-1:
        dx,dy=x+move[mindind][0],y+move[mindind][1]
        visited[dx][dy]=True
        if dfs(dx,dy,step+1):
            return True
        visited[dx][dy]=False
    return False

n=int(input())
sr,sc=map(int,input().split())    
visited=[[False]*(n+1) for i in range(n+1)]
visited[sr+1][sc+1]=True
flag=dfs(sr+1,sc+1,1)
print("success" if flag else "fail")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240415194822710](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240415194822710.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

期中！寄！

