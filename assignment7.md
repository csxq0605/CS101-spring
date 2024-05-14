# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

2024 spring, Complied by ==苏王捷 工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：Spyder IDE 5.5.2



## 1. 题目

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/



思路：直接一个列表倒序



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:28:51 2024

@author: Lenovo
"""

print(*(list(input().split())[::-1]))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240403161710143](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240403161710143.png)



### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/



思路：用字典测词汇是不是在列表内



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:10:39 2024

@author: Lenovo
"""

from collections import deque
m,n=map(int,input().split())
l=list(map(int,input().split()))
s=set()
queue=deque()
length=ans=0
for num in l:
    if num not in s and length<m:
        ans+=1
        length+=1
        s.add(num)
        queue.append(num)
    elif num not in s and length==m:
        s.add(num)
        queue.append(num)
        ans+=1
        p=queue.popleft()
        s.discard(p)
print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240403161800691](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240403161800691.png)



### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：绷，卡的最久的一题，要考虑k的特殊情况，还有1的可行性



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:13:40 2024

@author: Lenovo
"""

n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
if k==0:
    if l[0]>1:print(1)
    else:print(-1)
elif k<n and n>1 and l[k-1]==l[k]:
    print(-1)
else:
    print(l[k-1])

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403161852828](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240403161852828.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/



思路：递归建树，判断节点字母，后序输出



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:18:35 2024

@author: Lenovo
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None

def build(s):
    if len(s)==1:
        return Node("B") if s=="0" else Node("I")
    if "0"*len(s)==s:    
        node=Node("B")
    elif "1"*len(s)==s:
        node=Node("I")
    else:
        node=Node("F")
    node.lchild=build(s[0:len(s)//2])
    node.rchild=build(s[len(s)//2:])
    return node

def postorder(root):
    if root is None:
        return
    postorder(root.lchild)
    postorder(root.rchild)
    print(root.value,end="")

n=int(input())
s=input()
tree=build(s)
postorder(tree)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403161936820](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240403161936820.png)



### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/



思路：套了n壳让代码变得十分难懂，下简述

dic记录学生对应的组别，vis记录现有队列内同组学生的人数，cnt模拟队头将一个组的学生完全pop出时进入下一组，ind记录队列内各组学生的位置，队列内同组学生共占一个位置，组内顺序按添加顺序，出队时从队列头部的同组中出一个，如果此时组内无人则cnt+1进入下一组，添加时如有人则加入到对应位置的组内，无人将组别加在队尾记录位置



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:25:37 2024

@author: Lenovo
"""

from collections import deque
t=int(input())
dic,vis={},[0]*t
for i in range(t):
    l=list(input().split())
    for stu in l:
        dic[stu]=i
cnt,ind,queue=0,{},[]
while True:
    s=input().split()
    if s[0]=="STOP":
        break
    elif s[0]=="DEQUEUE":
        num=queue[cnt].popleft()
        vis[dic[num]]-=1
        if not vis[dic[num]]:
            cnt+=1
        print(num)
    else:
        num=s[1]
        if vis[dic[num]]:
            queue[ind[dic[num]]].append(num)
        else:
            ind[dic[num]]=len(queue)
            queue.append(deque([num]))
        vis[dic[num]]+=1

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403162608149](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240403162608149.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/



思路：这个节点的读入顺序就让我很难建树，于是直接用字典记录节点，用节点大小直接指代节点，用集合差集找到初始根节点，最后的排序递归输出顺序



代码

```python
# # -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:48:08 2024

@author: Lenovo
"""

def order(root):
    if dic[root] is None:
        print(root)
        return
    l=dic[root]
    l.append(root)
    l.sort()
    for num in l:
        if num==root:
            print(num)
        else:
            order(num)

n=int(input())
dic,vis1,vis2={},set(),set()
for i in range(n):
    l=list(map(int,input().split()))
    if len(l)==1:
        dic[l[0]]=None
    else:
        dic[l[0]]=l[1:]
        for x in l[1:]:    
            vis2.add(x)
    for x in l:        
        vis1.add(x)
for x in (vis1-vis2):
    root=x
order(root)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240403162553903](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240403162553903.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

感觉每次考试都会反而在前面的题卡顿，晕

各种特殊情况的考虑仍然比较复杂也更困难

题库内出现了图搜索的新题，是要图搜索了吗？在此先裂墙推荐heapq



