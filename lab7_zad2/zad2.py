from dimacs import *
import networkx as nx
from networkx.algorithms.flow import maximum_flow
def graph(G):
    for u,v ,w in L:
        G.add_edge(u,v)
        G[u][v]['capacity']=w


G = nx.Graph()
(V, L) = loadDirectedWeightedGraph("clique5")
graph(G)
print(maximum_flow( G, 1, 3))