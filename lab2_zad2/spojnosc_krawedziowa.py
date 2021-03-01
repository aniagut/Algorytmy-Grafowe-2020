from dimacs import *
from collections import deque

def tomatrix(V,L):
    G=[[0 for i in range (V)] for j in range(V)] # poczatkowa przepustowosc 0 dla kazdej pary wierzcholkow
    for x,y,z in L:
        G[x-1][y-1]=z
        G[y-1][x-1]=z
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

def spojnosc(V,L):
    MIN=float('inf')
    for s in range (V):
        for t in range (s+1,V):
            G=tomatrix(V,L)
            maxflow=0
            parents = [None] * V
            while BFS(G,V,s,t,parents):
                curr_flow=float('inf')
                fin=t
                while fin!=s:
                    curr_flow=min(curr_flow,G[parents[fin]][fin])
                    fin=parents[fin]
                maxflow+=curr_flow
                fin=t
                while fin!=s:
                    G[parents[fin]][fin]-=curr_flow
                    G[fin][parents[fin]]+=curr_flow
                    fin=parents[fin]
            if (maxflow!=0 and maxflow<MIN):
                MIN=maxflow
    return MIN
(V, L) = loadDirectedWeightedGraph("clique5");
print(spojnosc(V,L))