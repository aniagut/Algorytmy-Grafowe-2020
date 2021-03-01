from dimacs import *
from collections import deque

def tomatrix(V,L):
    G=[[0 for i in range (V)] for j in range(V)] # poczatkowa przepustowosc 0 dla kazdej pary wierzcholkow
    for x,y,z in L:
        G[x-1][y-1]=z
    return G

def BFS(G,V,s,t,parents):
    visited=[False]*V
    Q=deque()
    Q.append(s)
    visited[s]=True
    while Q:
        x=Q.popleft()
        for i in range (V):
            if G[x][i]>0 and visited[i]==False:
                Q.append(i)
                visited[i]=True
                parents[i]=x
    if visited[t]==True:
        return True
    else: return False

def DFS(G,V,s,t,parents,visited):
    if s==t: return True
    visited[s]=True
    for i in range(V):
        if G[s][i]>0 and visited[i]==False:
            parents[i]=s
            if DFS(G,V,i,t,parents,visited):
                return True

    return False

def maxflow_BFS(G,V):
    parents=[None]*V
    max_flow=0
    while BFS(G,V,0,V-1,parents):
        curr_flow=float('inf')
        fin=V-1
        while fin!=0:
            curr_flow=min(curr_flow,G[parents[fin]][fin])
            fin=parents[fin]
        max_flow+=curr_flow
        fin=V-1
        while fin!=0:
            G[parents[fin]][fin]-=curr_flow
            G[fin][parents[fin]]+=curr_flow
            fin=parents[fin]
    return max_flow

def maxflow_DFS(G,V):
    parents=[None]*V
    visited=[False]*V
    max_flow=0
    while DFS(G,V,0,V-1,parents,visited):
        curr_flow = float('inf')
        fin = V - 1
        while fin != 0:
            curr_flow = min(curr_flow, G[parents[fin]][fin])
            fin = parents[fin]
        max_flow += curr_flow
        fin = V - 1
        while fin != 0:
            G[parents[fin]][fin] -= curr_flow
            G[fin][parents[fin]] += curr_flow
            fin = parents[fin]
        parents=[None]*V
        visited=[False]*V
    return max_flow



(V,L)=loadDirectedWeightedGraph("pp100");
G=tomatrix(V,L)
G1=tomatrix(V,L)
print(maxflow_BFS(G,V))
print(maxflow_DFS(G1,V))


