# Assignment #B: 图论和树算

Updated 1709 GMT+8 Apr 28, 2024

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

### 28170: 算鹰

dfs, http://cs101.openjudge.cn/practice/28170/



思路：鹰？Lake！Lake Counting



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:57:46 2024

@author: Lenovo
"""

grid=[]
for _ in range(10):
    row=list(input().strip())
    grid.append(row)
visited=[[False]*10 for _ in range(10)]  
dir_x=[-1,0,1,0] 
dir_y=[0,-1,0,1]
pondCount = 0
for i in range(10):
    for j in range(10):
        if grid[i][j]=='.' and not visited[i][j]:
            pondCount+=1
            stack=[(i,j)]
            visited[i][j]=True
            while stack:
                x,y=stack.pop()
                for k in range(4):
                    nx,ny=x+dir_x[k],y+dir_y[k]
                    if nx>=0 and nx<10 and ny>=0 and ny<10 and grid[nx][ny]=='.' and not visited[nx][ny]:
                        stack.append((nx,ny))
                        visited[nx][ny]=True
print(pondCount)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240429195818364](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240429195818364.png)



### 02754: 八皇后

dfs, http://cs101.openjudge.cn/practice/02754/



思路：dfs 记录路径



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:48:19 2023

@author: Lenovo
"""

hang=[0]*8
ans=[[0]*8 for _ in range(92)]
num=0
def queen(n):
    global num
    if n==8:
        for i in range(8):
            ans[num][i]=hang[i]+1
        num+=1
        return
    for i in range(8):
        for j in range(n):
            if i==hang[j] or (j-n)==hang[j]-i or (n-j)==hang[j]-i:
                break
        else:
            hang[n]=i
            queen(n+1)
queen(0)
n=int(input())
for _ in range(n):
    b=int(input())
    for i in range(8):
        print(ans[b-1][i],end="")
    print()

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240429195859471](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240429195859471.png)



### 03151: Pots

bfs, http://cs101.openjudge.cn/practice/03151/



思路：分情况记录加入队列，找到可能



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:12:27 2024

@author: Lenovo
"""

import heapq
a,b,c=map(int,input().split())
heap=[]
vis=set()
flag=False
heapq.heappush(heap,(0,0,0,""))
vis.add((0,0))
move=["FILL(1)","FILL(2)","DROP(1)","DROP(2)","POUR(1,2)","POUR(2,1)"]
while heap:
    step,l1,l2,path=heapq.heappop(heap)
    if l1==c or l2==c:
        flag=True
        break
    if l1<a and (a,l2) not in vis:
        heapq.heappush(heap,(step+1,a,l2,path+"0"))
        vis.add((a,l2))
    if l2<b and (l1,b) not in vis:
        heapq.heappush(heap,(step+1,l1,b,path+"1"))
        vis.add((l1,b))
    if l1>0 and (0,l2) not in vis:
        heapq.heappush(heap,(step+1,0,l2,path+"2"))
        vis.add((0,l2))
    if l2>0 and (l1,0) not in vis:
        heapq.heappush(heap,(step+1,l1,0,path+"3"))
        vis.add((l1,0))
    if l1>0 and l2<b and (l1+l2-min(l1+l2,b),min(l1+l2,b)) not in vis:
        heapq.heappush(heap,(step+1,l1+l2-min(l1+l2,b),min(l1+l2,b),path+"4"))
        vis.add((l1+l2-min(l1+l2,b),min(l1+l2,b)))
    if l1<a and l2>0 and (min(l1+l2,a),l1+l2-min(l1+l2,a)) not in vis:
        heapq.heappush(heap,(step+1,min(l1+l2,a),l1+l2-min(l1+l2,a),path+"5"))
        vis.add((min(l1+l2,a),l1+l2-min(l1+l2,a)))
if flag:
    print(step)
    for i in path:
        print(move[int(i)])
else:
    print("impossible")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240429200029515](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240429200029515.png)



### 05907: 二叉树的操作

http://cs101.openjudge.cn/practice/05907/



思路：建树，实现交换和查询



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:36:06 2024

@author: Lenovo
"""

class Node:
    def __init__(self):
        self.lchild=None
        self.rchild=None
        self.parent=None

def exchange(x,y):
    px,py=tree[x].parent,tree[y].parent
    if px==py:
        if tree[px].lchild==x:
            tree[px].lchild,tree[px].rchild=y,x
        else:
            tree[px].lchild,tree[px].rchild=x,y
    else:
        if tree[px].lchild==x:
            tree[px].lchild=y
        else:
            tree[px].rchild=y
        tree[y].parent=px
        if tree[py].lchild==y:
            tree[py].lchild=x
        else:
            tree[py].rchild=x
        tree[x].parent=py

def search(x):
    while tree[x].lchild!=-1:
        x=tree[x].lchild
    print(x)

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    tree=[Node() for i in range(n+1)]
    for i in range(n):
        a,la,ra=map(int,input().split())
        tree[a].lchild,tree[a].rchild=la,ra
        tree[la].parent=tree[ra].parent=a
    for i in range(m):
        l=list(map(int,input().split()))
        if l[0]==1:
            x,y=l[1],l[2]
            exchange(x,y)
        else:
            x=l[1]
            search(x)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240429200148926](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240429200148926.png)





### 18250: 冰阔落 I

Disjoint set, http://cs101.openjudge.cn/practice/18250/



思路：并查集



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:01:49 2024

@author: Lenovo
"""

class DisjSet:
    def __init__(self,n):
        self.pre=[i for i in range(n+1)]
    
    def find(self,x):
        if x==self.pre[x]:
            return x
        self.pre[x]=self.find(self.pre[x])
        return self.pre[x]

    def union(self,x,y):
        rootx,rooty=self.find(x),self.find(y)
        if rootx==rooty:
            return True
        else:
            self.pre[rooty]=rootx
            return False
    
while True:
    try:
        n,m=map(int,input().split())
        s=DisjSet(n)
        for i in range(m):
            x,y=map(int,input().split())
            flag=s.union(x,y)
            print("Yes" if flag else "No")
        count,ans=0,[]
        for i in range(1,n+1):
            if i==s.pre[i]:
                count+=1
                ans.append(i)
        print(count)
        print(*ans)
    except EOFError:
        break

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240429200238593](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240429200238593.png)



### 05443: 兔子与樱花

http://cs101.openjudge.cn/practice/05443/



思路：图搜索dfs，记录路径及距离，用中间路径剪枝



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:35:01 2024

@author: Lenovo
"""

minlen,totallen,ans=float("inf"),0,[]
def dfs(s,t):
    global totallen,minlen,ans
    if s==t:
        if totallen<minlen:
            ans=tmp.copy()
        return
    for road in citymap[s]:
        d,l=road['d'],road['l']
        if d in visited:
            continue
        length=l+totallen
        if length>=minlen or length>=minl[d]:
            continue
        totallen=length
        minl[d]=length
        visited.add(d)
        tmp.append("("+str(l)+")")
        tmp.append(d)
        dfs(d,t)
        totallen-=l
        visited.discard(d)
        tmp.pop()
        tmp.pop()

p=int(input())
destinations=[input() for _ in range(p)]
q=int(input())
citymap={i:[] for i in destinations}
for i in range(q):
    s,d,l=map(str,input().split())
    citymap[s].append({"d":d,"l":int(l)})
    citymap[d].append({"d":s,"l":int(l)})
r=int(input())
for _ in range(r):
    s,t=input().split()
    minl={i:float("inf") for i in destinations}
    minlen,totallen,ans,tmp=float("inf"),0,[],[s]
    visited=set()
    visited.add(s)
    dfs(s,t)
    print("->".join(ans))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240429200420156](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240429200420156.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

准备转系考，竞争激烈啊

Wish  me good luck!



