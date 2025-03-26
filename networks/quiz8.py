import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
edge_list = [
   ('e','c'),     
   ('c','f'), 
   ('f','i'), 
   ('i','e'), 
   ('i','k'), 
   ('k','j'), 
   ('f','g'), 
   ('g','d'), 
   ('d','h'), 
   ('h','j'), 
   ('j','g')    
]
G.add_edges_from(edge_list)
print(nx.clustering(G,['g','d','h','j']))
nx.draw(G)
plt.show()