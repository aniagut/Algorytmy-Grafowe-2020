from dimacs import *
import networkx as nx
from networkx.algorithms.planarity import check_planarity


def graph(G):
    for u,v ,w in L:
        G.add_edge(u,v)


G = nx.Graph()
(V, L) = loadDirectedWeightedGraph("clique5")
graph(G)
print(check_planarity(G))