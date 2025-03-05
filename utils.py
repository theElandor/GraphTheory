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
    
def bfs_undirected(G, start, return_tuple=False):
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
    if return_tuple:
        tuple_dist = []
        for k,v in dist.items():
            tuple_dist.append((k,v))
        return sorted(tuple_dist, key=lambda x:x[0])
    else:
        return dist

def closeness_centrality_undirected(G:dict, v) -> int:
    """
    Args:
       -G: Graph
       -v: ID of the source node
   Return:
       -closeness centrality for specified node
    """
    dist = bfs_undirected(G, v, return_tuple=True)
    return 1/sum([y for x,y in dist if x != v])


def get_all_paths(G, s:int, d:int, sp:int):
    """
    Args:
        -G: Graph
        -s: source node
        -d: destination node
        -sp: shortest path between u and v
    Return:
        -list of all possible paths from u to v with length = sp
    """
    Q = deque()
    Q.append((0, s, str(s)))
    sol = []
    while Q:
        distance, current, path = Q.popleft()
        if distance > sp:
            continue
        elif distance == sp and current == d:
            sol.append(path)
        else:
            for v in G[current]:
                Q.append((distance+1, v, path+ f" {v}"))
    return sol

def betweennes_centrality_undirected(G:dict, v):
    """
    Args:
        -G: Graph
        -v: ID of the source node
    Return:
        -betweennes centrality for specified node

    For now we just use plain BFS to compute distances between
    pairs of nodes. It is very expensive and not efficient, it would
    be better to pre-compute the distance between any pair of nodes
    using floyd-warshall or a similar algorithm.
    """
    # assuming graph is connected here
    
    nodes = G.keys()
    score = 0
    done = set()
    for s in nodes:
        for t in nodes:
            if t == v or s==v or  t == s or (t,s) in done or (s,t) in done: continue
            done.add((s,t))
            done.add((t,s))
            # get distance between u and v
            dist = bfs_undirected(G, s)
            dist_s_t = dist[t]
            print(f"Paths for {s}-{t}")
            possible_paths = get_all_paths(G, s, t, dist_s_t)
            print(possible_paths)
            denominator = len(possible_paths)
            numerator = 0
            for path in possible_paths:
                if str(v) in path.split(" "):
                    numerator += 1
            #print(f"adding {numerator}/{denominator}")
            score += (numerator / denominator)
    return score
