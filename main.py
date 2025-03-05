from utils import *
edges = read_graph("network.txt")
G = build_undirected(edges)
plot_graph(edges)
# ============ closeness centrality for node 1 ===========
dist = bfs_undirected(G, 1)
print_nn_dist(dist)
print(closeness_centrality_undirected(dist,1))
# ============ betweennes centrality for node 1 ==========

