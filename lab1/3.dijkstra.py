from dimacs import *
from queue import PriorityQueue
def create(G,L):
    for u, v, c in L:
        u -= 1
        v -= 1
        G[u].append((v, c))
        G[v].append((u, c))

def fu(V,L):
    G = [[] for i in range(V)]
    create(G, L)
    Q=PriorityQueue()
    for x,c in G[0]:
        Q.put((-c,x))
    min=float('inf')
    visited=[False]*V
    visited[0]=True
    while not Q.empty():
        a=Q.get()
        visited[a[1]]=True
        if a[0]*(-1)<min:
            min=a[0]*(-1)
        if a[1]==V-1:
            return min
        for x,c in G[a[1]]:
            if visited[x]==False:
                Q.put((-c, x))
    return -1




(V, L) = loadWeightedGraph("clique5")
print(fu(V,L))