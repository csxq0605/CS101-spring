# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:01:34 2024

@author: Lenovo
"""

def toposort(nodes,graph):
    def dfs1(x):
        for i in graph[x]:
            if i not in vis:
                ind[i]-=1
        cnt=0
        for i in graph[x]:
            if i not in vis and ind[i]==0:
                u=i
                cnt+=1
        if cnt==1:
            vis.add(u)
            dfs1(u)
        elif cnt>=2:
            return
    
    def dfs2(x):
        for i in graph[x]:
            if i not in vis:
                ind[i]-=1
                if not ind[i]:
                    vis.add(i)
                    dfs2(i)
    
    ind=indegree.copy()
    vis=set()
    for node in nodes:
        if ind[node]==0 and node not in vis:
            vis.add(node)
            dfs1(node)
            break
    flag1=(len(vis)==len(nodes))
    ind=indegree.copy()
    vis=set()
    for node in nodes:
        if ind[node]==0 and node not in vis:
            vis.add(node)
            dfs2(node)
    flag2=(len(vis)==len(nodes))
    return flag1,flag2

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    Edge=[tuple(input().split("<")) for i in range(m)]
    indegree={chr(i):0 for i in range(65,65+n)}
    graph={chr(i):[] for i in range(65,65+n)}
    nodes=set()
    flag=False
    for i in range(m):
        e,s=Edge[i]
        graph[s].append(e)
        indegree[e]+=1
        nodes.add(s)
        nodes.add(e)
        if s==e:
            flag2=False
        else:    
            flag1,flag2=toposort(nodes,graph)
        if not flag2:
            print(f"Inconsistency found after {i+1} relations.")
            flag=True
            break
        elif flag1 and len(nodes)==n:
            vis=set()
            cnt=0
            ans=[]
            while cnt<n:
                for node in nodes:
                    if indegree[node]==0 and node not in vis:
                        vis.add(node)
                        ans.append(node)
                        cnt+=1
                        for no in graph[node]:
                            indegree[no]-=1
                        break
            ans="".join(ans[::-1])
            print(f"Sorted sequence determined after {i+1} relations: {ans}.")
            flag=True
            break
    if not flag:
        print("Sorted sequence cannot be determined.")