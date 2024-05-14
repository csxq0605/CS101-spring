# Assignment #A: 图论：遍历，树算及栈

Updated 2018 GMT+8 Apr 21, 2024

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

### 20743: 整人的提词本

http://cs101.openjudge.cn/practice/20743/



思路：栈实现翻转



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:51:54 2024

@author: Lenovo
"""

s=input()
stack=[]
for _ in s:
    if _==")":
        temp=[]
        while stack and stack[-1]!="(":
            temp.append(stack.pop())
        if stack:
            stack.pop()
        stack.extend(temp)
    else:
        stack.append(_)
print("".join(stack))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240422203026473](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240422203026473.png)



### 02255: 重建二叉树

http://cs101.openjudge.cn/practice/02255/



思路：根据前中序建树



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:57:44 2024

@author: Lenovo
"""

def loge(front,mid,length):
    if length==0:
        return
    if length==1:
        print(front[0],end="")
        return
    top=front[0]
    i=0
    while mid[i]!=top:
        i+=1
    loge(front[1:],mid,i)
    loge(front[i+1:],mid[i+1:],length-i-1)
    print(top,end="")
while True:
    try:
        front,mid=map(str,input().split())
        length=len(front)
        loge(front,mid,length)
        print()
    except:
        break

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240422203107736](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240422203107736.png)



### 01426: Find The Multiple

http://cs101.openjudge.cn/practice/01426/

要求用bfs实现



思路：对余数进行bfs



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:45:09 2024

@author: Lenovo
"""

from collections import deque
while True:
    n=int(input())
    if n==0:
        break
    q=deque()
    vis=set()
    q.append((1,1))
    vis.add(1)
    while q:
        r,num=q.popleft()
        if r==0:
            print(num)
            break
        for i in range(2):
            dr=(r*10+i)%n
            if dr not in vis:
                vis.add(dr)
                q.append((dr,num*10+i))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240422203140998](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240422203140998.png)



### 04115: 鸣人和佐助

bfs, http://cs101.openjudge.cn/practice/04115/



思路：bfs图搜索



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:13:27 2023

@author: Lenovo
"""

from collections import deque
class Node:
    def __init__(self,x,y,tools,steps):
        self.x=x
        self.y=y
        self.tools=tools
        self.steps=steps

M,N,T=map(int,input().split())
maze=[list(input()) for _ in range(M)]
visit=[[[0]*(T+1) for _ in range(N)] for _ in range(M)]
directions=[[-1, 0],[1, 0],[0, -1],[0, 1]]
start=end=None
flag=0
for i in range(M):
    for j in range(N):
        if maze[i][j]=='@':
            start=Node(i,j,T,0)
            visit[i][j][T]=1
        if maze[i][j]=='+':
            end=(i,j)
            maze[i][j]='*'
queue=deque([start])
while queue:
    node=queue.popleft()
    if (node.x,node.y)==end:
        print(node.steps)
        flag=1
        break 
    for direction in directions:
        nx,ny=node.x+direction[0],node.y+direction[1]
        if 0<=nx<M and 0<=ny<N:
            if maze[nx][ny]=='*':
                if not visit[nx][ny][node.tools]:
                    queue.append(Node(nx,ny,node.tools,node.steps+1))
                    visit[nx][ny][node.tools]=1
            elif maze[nx][ny]=='#':
                if node.tools>0 and not visit[nx][ny][node.tools-1]:
                    queue.append(Node(nx,ny,node.tools-1,node.steps+1))
                    visit[nx][ny][node.tools-1]=1
if not flag:
    print("-1")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240422203238623](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240422203238623.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/



思路：heapq！



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:48:27 2023

@author: Lenovo
"""

import heapq
m,n,p=map(int,input().split())
martix=[list(input().split())for i in range(m)]
dir=[(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(p):
    sx,sy,ex,ey=map(int,input().split())
    if martix[sx][sy]=="#" or martix[ex][ey]=="#":
        print("NO")
        continue
    vis,heap,ans=set(),[],[]
    heapq.heappush(heap,(0,sx,sy))
    vis.add((sx,sy,-1))
    while heap:
        tire,x,y=heapq.heappop(heap)
        if x==ex and y==ey:
            ans.append(tire)
        for i in range(4):
            dx,dy=dir[i]
            x1,y1=dx+x,dy+y
            if 0<=x1<m and 0<=y1<n and martix[x1][y1]!="#" and (x1,y1,i) not in vis:
                t1=tire+abs(int(martix[x][y])-int(martix[x1][y1]))
                heapq.heappush(heap,(t1,x1,y1))
                vis.add((x1,y1,i))
    print(min(ans) if ans else "NO")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240422203410059](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240422203410059.png)



### 05442: 兔子与星空

Prim, http://cs101.openjudge.cn/practice/05442/



思路：用并查集想法实现连通图



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:09:18 2024

@author: Lenovo
"""

class Edge:
    def __init__(self,f,t,c):
        self.f=f
        self.t=t
        self.cost=c
    def __lt__(self,other):
        return self.cost<other.cost

def find(x,fa):
    if fa[x]==-1:
        return x
    return find(fa[x],fa)

n=int(input())
edges=[]
for i in range(n-1):
    line=list(input().split())
    k=int(line[1])
    for j in range(k):
        ch,cost=line[2*j+2],int(line[2*j+3])
        edges.append(Edge(i,ord(ch)-65,cost))
edges.sort()
fa=[-1]*30
ans=cnt=0
for i in range(len(edges)):
    if cnt==n-1:
        break
    e=edges[i]
    if find(e.f,fa)!=find(e.t,fa):
        ans+=e.cost
        cnt+=1
        fa[find(e.t,fa)]=find(e.f,fa)
print(ans)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240422203602707](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240422203602707.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

Kruscal和Prim算法要来力吗？

期中被数学深刻打击震撼于是原地准备转码，wish me good luck！

