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

def isPEO(G,vs):
    sets=[set() for i in range (V+1)]
    for i in range (1,V+1):
        idx=0
        for j in range(len(vs)):
            if vs[j]==i:
                idx=j
            for k in range (idx):
                if vs[k] in G[i].out:
                    sets[i].add(vs[k])
    for i in range (1,V+1):
        if(len(sets[i])>0):
            parent=-1
            for element in sets[i]:
                parent=element
            if not (sets[i]-{parent})&sets[parent]==(sets[i]-{parent}):
                return False
    return True


def checkLexBFS(G, vs):
  n = len(G)
  pi = [None] * n
  for i, v in enumerate(vs):
    pi[v] = i

  for i in range(n-1):
    for j in range(i+1, n-1):
      Ni = G[vs[i]].out
      Nj = G[vs[j]].out

      verts = [pi[v] for v in Nj - Ni if pi[v] < i]
      if verts:
        viable = [pi[v] for v in Ni - Nj]
        if not viable or min(verts) <= min(viable):
          return False
  return True

def isChordal(G):
    vs=lexBFS(G)
    return checkLexBFS(G,vs)

(V, L) = loadWeightedGraph("interval-rnd6")
G = [None] + [Node(i) for i in range(1, V+1)]  # żeby móc indeksować numerem wierzchołka

for (u, v, _) in L:
  G[u].connect_to(v)
  G[v].connect_to(u)

print(isChordal(G))