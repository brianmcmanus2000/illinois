import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt

def calculate_edge_betweenness(G):
    betweenness = defaultdict(float)
    all_shortest_paths = dict(nx.all_pairs_all_shortest_paths(G))
    for source, target_paths in all_shortest_paths.items():
        for target, paths in target_paths.items():
            if source == target:
                continue
            num_paths = len(paths)
            for path in paths:
                for i in range(len(path) - 1):
                    edge = (path[i], path[i + 1])
                    betweenness[edge] += 1.0 / num_paths
    for edge in betweenness:
        betweenness[edge] /= 2 
    return dict(betweenness)

edge_list = [('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','g'),
     ('g','h'),('h','i'),('i','j'),('j','k'),('k','l'),('l','m'),
     ('m','n'),('n','o'),('o','p'),('p','q'),('q','r'),('r','s')]
G = nx.Graph()
G.add_edges_from(edge_list)
mine = calculate_edge_betweenness(G)
theirs = nx.edge_betweenness_centrality(G, normalized=True)
print(mine)
print(theirs)
nx.draw(G)
plt.show()