import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
edge_list = [('a','b'),('a','c'),('c','b'),('d','g'),('g','f'),('f','e'),('e','d'),('d','f')]

G.add_edges_from(edge_list)
constant = (4*G.number_of_nodes())
betweenness = nx.edge_betweenness_centrality(G, normalized=True)
print(betweenness)

betweenness = nx.edge_betweenness_centrality(G, normalized=False)
print(betweenness)

for edge,weight in betweenness.items():
    betweenness[edge] = weight/constant
print(betweenness)

nx.draw(G, with_labels=True)
plt.show()