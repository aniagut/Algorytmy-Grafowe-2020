from dimacs import *
from queue import PriorityQueue


class Node:
  def __init__(self):
    self.edges = {}
    self.deactivated=False
    self.merged=[]

  def addEdge( self, to, weight):
    self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                    # o zadanej wadze; a jeśli taka krawędź
                                                    # istnieje, to dodaj do niej wagę

  def delEdge( self, to ):
    del self.edges[to]      # usuń krawędź do zadanego wierzchołka

def make_graph(V,L):
    G = [ Node() for i in range(V)]
    for (x,y,c) in L:
      G[x-1].addEdge(y-1,c)
      G[y-1].addEdge(x-1,c)
    return G

def print_(G,V):
    for i in range(V):
        print( i, G[i].edges)

def mergeVertices(G,x,y):
    #usuwa z y i dodaje do x
    list=G[y].edges
    for i in list:
        if(i!=x):
            w = G[y].edges.get(i, 0)
            G[x].addEdge(i,w)
            G[i].delEdge(y)
            G[i].addEdge(x,w)
    G[y].deactivated=True
    G[x].delEdge(y)

def minimumCutPhase(G,n,V):
    a = 0
    S = []
    Q=PriorityQueue()
    Q.put((a,0))
    processed=[False]*V
    weights=[0]*V
    lw=0
    while len(S)!=n:
        q=Q.get()
        lw=weights[q[0]]
        if not processed[q[0]]:
            processed[q[0]]=True
            S.append(q[0])
            for v in G[q[0]].edges:
                if not processed[v] and not G[v].deactivated:
                    w=G[q[0]].edges.get(v,0)
                    weights[v]+=w
                    Q.put((v,weights[v]))
    s=S[n-2]
    t=S[n-1]
    mergeVertices(G,s,t)
    return lw,(s,t)

def Stoer_Wagner(G,V):
    n=len(G)-3
    len1 = V - 1
    lw,a=minimumCutPhase(G,len1,V)
    len1-=1
    while n!=0:
        cw,xy=minimumCutPhase(G,len1,V)
        if cw<lw:
            lw=cw
            a=xy
        n-=1
        len1-=1
    return lw







(V,L) = loadWeightedGraph( "clique100" )
G=make_graph(V,L)
print_(G,V)
print()
print(Stoer_Wagner(G,V))

