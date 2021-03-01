from dimacs import *

def create(G,L):
    for u, v, c in L:
        u -= 1
        v -= 1
        G[u].append((v, c))
        G[v].append((u, c))

def wypisz(G,V):
    for u in range(1, V + 1):
        s = f"{u}: "
        for v in G[u-1]:
            s += f"{(v[0]+1,v[1])}, "
        print(s)


def find_set(x,parents):
        if x != parents[x]:
            parents[x] = find_set(parents[x],parents)
        return parents[x]

def union(x, y,parents,rank):
        x = find_set(x,parents)
        y = find_set(y,parents)
        if rank[x] > rank[y]:
            parents[y] = x
        else:
            parents[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

def fu(V,L):
    parents=[x for x in range (V)]
    rank=[0]*V
    m=len(L)
    L1=L
    for i in range(m):
        L1[i]=(L1[i][0],L1[i][1],-L1[i][2])
    L1.sort(key=lambda x:x[2])
    for x, y, c in L1:
        union(x-1,y-1,parents,rank)
        if find_set(0,parents)==find_set(V-1,parents):
            return -c
    return -1

(V,L)=loadWeightedGraph("clique5")
G = [[] for i in range(V)]
create(G,L)
wypisz(G,V)
print(fu(V,L))
