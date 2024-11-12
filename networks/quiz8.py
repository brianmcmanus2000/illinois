import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6])
G.add_edges_from([(1,2),(1,3),(1,5)])
G.add_edges_from([(2,1),(2,3),(2,4)])
G.add_edges_from([(3,1),(3,2),(3,6)])
G.add_edges_from([(4,2),(4,5),(4,6)])
G.add_edges_from([(5,1),(5,4),(5,6)])
G.add_edges_from([(6,3),(6,4),(6,5)])
print(nx.average_clustering(G))
nx.draw(G)
plt.show()