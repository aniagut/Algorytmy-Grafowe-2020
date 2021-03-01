from dimacs import *

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()

    def connect_to(self, v):
        self.out.add(v)

def lexBFS(G):
    sets=[set(range(1,len(G)))]
    visited=[]
    while len(sets)>0:
        curr=sets[-1].pop()
        visited.append(curr)
        partition=[]
        for to_part in sets:
            reachable = to_part & G[curr].out
            unreachable = to_part - G[curr].out
            if len(unreachable)>0:
                partition.append(unreachable)
            if len(reachable) > 0:
                partition.append(reachable)
        sets=partition
    return visited

def maxcliquesize(G):
    vs=lexBFS(G)
    print(vs)
    sets = [set() for i in range(V + 1)]
    for i in range(1, V + 1):
        idx = 0
        for j in range(len(vs)):
            if vs[j] == i:
                idx = j
            for k in range(idx):
                if vs[k] in G[i].out:
                    sets[i].add(vs[k])
    max=0
    for set1 in sets:
        if len(set1)>max:
            max=len(set1)
    return max

(V, L) = loadWeightedGraph("simple-noninterval1")
G = [None] + [Node(i) for i in range(1, V+1)]  # żeby móc indeksować numerem wierzchołka
for (u, v, _) in L:
  G[u].connect_to(v)
  G[v].connect_to(u)
print(maxcliquesize(G))
