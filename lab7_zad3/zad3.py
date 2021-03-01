from dimacs import *
import networkx as nx
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort

#Budowa grafu implikacji
def graph(G,F):
    for x,y in F:
        if not G.has_edge(-x,y):
            G.add_edge(-x,y)
        if not G.has_edge(-y,x):
            G.add_edge(-y,x)


G = nx.DiGraph()
(V,F) = loadCNFFormula("simple_sat")
print(F)
graph(G,F)
print(G.nodes)
print(G.edges)

O = topological_sort(G)
SCC = strongly_connected_components(G)


