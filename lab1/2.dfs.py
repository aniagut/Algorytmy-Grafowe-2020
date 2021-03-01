from dimacs import *

def create(G,L):
    for u, v, c in L:
        u -= 1
        v -= 1
        G[u].append((v, c))
        G[v].append((u, c))


def DfSvisit(G,v,visited,parents,V,min):
    visited[v] = True
    for i, c in G[v]:
        if c>=min:
            if visited[i] == False:
                parents[i] = v
                DfSvisit(G,i,visited,parents,V,min)
def DFS(G,V,min):
    visited=[False]*V
    parents=[None]*V
    DfSvisit(G,0,visited,parents,V,min)
    if visited[V-1]==True:
        return True

def fu(V,L):
    G = [[] for i in range(V)]
    create(G, L)
    L.sort(key=lambda x:x[2])
    m=len(L)
    min=float("-inf")
    p,k=0,m-1
    while p<=k:
        m=p+(k-p)//2
        curr=L[m][2]
        if DFS(G,V,curr):
            if curr>min:
                min=curr
            p=m+1
        else:
            k=m-1
    return min



(V, L) = loadWeightedGraph("clique5")
print(fu(V,L))