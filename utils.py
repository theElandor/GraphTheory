import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from prettytable import PrettyTable
def read_graph(file):
	"""!Function needed to read input graph.
	"""
	with open(file) as f:
		data = f.read().splitlines()
		edges = []
		for x in data:
			edges.append(tuple(eval(x)))
		return edges

def build_undirected(edges):
    G = {}
    for u,v in edges:
        if u not in G:
            G[u] = []
        if v not in G:
            G[v] = []
        G[u].append(v)
        G[v].append(u)
    return G

def plot_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def print_nn_dist(dist):
    x = PrettyTable()
    x.field_names = ["Destination", "Distance"]
    for s,d in dist:
        x.add_row([str(s), str(d)])
    print(x)
    
def bfs_undirected(G, start):
    dist = {}
    Q = deque()
    Q.append((0,start))
    while Q:
        distance, current = Q.popleft()
        if current not in dist:
            dist[current] = distance
        else:
            continue
        for v in G[current]:
            Q.append((distance+1, v))
    tuple_dist = []
    for k,v in dist.items():
        tuple_dist.append((k,v))
    return sorted(tuple_dist, key=lambda x:x[0])

def closeness_centrality_undirected(dist:list, v) -> int:
    """
    Args:
       -dist: list containing the distance from source node to other nodes.
       -v: ID of the source node.
   Return:
       -closeness: returns closeness centrality for specified node.
    """
    return 1/sum([y for x,y in dist if x != v])

def betweennes_centrality_undirected(dist:list, v):
    pass
