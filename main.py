import sys
filename = sys.argv[1]
from utils import *
edges = read_graph(filename)
G = build_undirected(edges)
#plot_graph(edges)
# ============ closeness centrality for node 1 ===========
print(closeness_centrality_undirected(G,1))
# ============ betweennes centrality for node 1 ==========
print(betweennes_centrality_undirected(G, 4))
