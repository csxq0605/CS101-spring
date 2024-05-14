# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:55:55 2024

@author: Lenovo
"""

from heapq import heappush,heappop
class Node:
    def __init__(self,x,y,pre,layer):
        self.x=x
        self.y=y
        self.pre=pre
        self.layer=layer
        
    def __lt__(self,other):
        return self.layer<other.layer

def print_path(node):
    path=[]
    while node.pre is not None:
        path.append(node)
        node=node.pre
    path.append(node)
    path=path[::-1]
    print('-'.join(f'({node.x},{node.y})' for node in path))

vis=[[-1]*11 for _ in range(11)]
pie=[[0]*11 for _ in range(11)]
step=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
q=[]
ansNum=0
ansNode=None
s_x,s_y=map(int,input().split())
e_x,e_y=map(int,input().split())
s=Node(s_x,s_y,None,0)
e=Node(e_x,e_y,None,0)
n=int(input())
for _ in range(n):
    tmp_x,tmp_y=map(int,input().split())
    pie[tmp_x][tmp_y]=1
vis[s.x][s.y]=0
heappush(q,s)
while q:
    old=heappop(q)
    if old.x==e.x and old.y==e.y:
        ansNode=old
        ansNum=1
        while q:
            node=heappop(q)
            if node.x==e.x and node.y==e.y and node.layer==ansNode.layer:    
                ansNum+=1
        if ansNum==1:
            print_path(ansNode)
        else:
            print(ansNum)
        break
    for i in range(8):
        now_x=old.x+step[i][0]
        now_y=old.y+step[i][1]
        now_layer=old.layer+1
        m_x=old.x+step[i][0]//2
        m_y=old.y+step[i][1]//2
        if 0<=now_x<11 and 0<=now_y<11 and not pie[now_x][now_y] and not pie[m_x][m_y] and (vis[now_x][now_y]==-1 or vis[now_x][now_y]==now_layer):
            q.append(Node(now_x,now_y,old,now_layer))
            vis[now_x][now_y]==now_layer