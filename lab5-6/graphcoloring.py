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

def graphcoloring(G):
    vs=lexBFS(G)
    color=[0 for i in range (V+1)]
    for v in vs:
        used=set()
        for u in G[v].out:
            if color[u] not in used:
                used.add(color[u])
        j=0
        while j in used:
            j+=1
        color[v]=j
    return color[1:V+1],max(color)


(V, L) = loadWeightedGraph("clique20")
G = [None] + [Node(i) for i in range(1, V+1)]  # żeby móc indeksować numerem wierzchołka

for (u, v, _) in L:
  G[u].connect_to(v)
  G[v].connect_to(u)

print(graphcoloring("house"))