import networkx as nx
from networkx.algorithms import bipartite
import csv
import matplotlib.pyplot as plt

# def get_preferences():
#     node_list = []
#     with open('preference.csv', newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
#         for row in spamreader:
#             node_list.append((row[0],{'preferences':row[1:None]}))
#     return node_list

# G = nx.Graph()
# buyers = get_preferences()
# houses = get_initial_prices()
# G.add_nodes_from(houses,bipartite=0)
# G.add_nodes_from(buyers,bipartite=1)

# We start with all hub scores and all authority scores equal to 1.
# We choose a number of steps, k.
# We then perform a sequence of k hub–authority updates. Each update works as
# follows:
# – First apply the Authority Update Rule to the current set of scores.
# – Then apply the Hub Update Rule to the resulting set of scores.
# At the end, the hub and authority scores may involve numbers that are very large.
# However, we only care about their relative sizes, so we can normalize to make
# them smaller: we divide down each authority score by the sum of all authority
# scores, and divide down each hub score by the sum of all hub scores.

# test1
# Top 3 Hubs : 1,2,3
# Top 3 Authorities: 1,2,3
# test2
# Top 3 Hubs: 12,2100,387
# Top 3 Authorities: 10897,21443,38976

def create_graph_from_file(filename:str):
    hubs = set()
    authorities = set()
    edges = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
        for row in spamreader:
            hubs.add("hub:"+str(row[0]))
            authorities.add("authority:"+str(row[1]))
            edges.append(("hub:"+str(row[0]),"authority:"+str(row[1])))
    G = nx.Graph()
    G.add_nodes_from(hubs,bipartite=0,weight=1)
    G.add_nodes_from(authorities,bipartite=1,weight=1)
    G.add_edges_from(edges)
    return G

G = create_graph_from_file("test1.txt")
hubs = [(n, d['weight']) for n, d in G.nodes(data=True) if d["bipartite"] == 0]
authorities = [(n, d['weight']) for n, d in G.nodes(data=True) if d["bipartite"] == 1]
hub_weights = [w for n, w in hubs]
authority_weights = [w for n, w in authorities]
for node, _ in hubs:
    G.nodes[node]['weight'] += 1
print(hub_weights)
hub_weights = [w for n, w in G.nodes(data=True) if G.nodes[n]["bipartite"] == 0]
print(hub_weights)

nx.draw_networkx(G, pos=nx.drawing.layout.bipartite_layout(G, [n for n, _ in hubs]))
plt.show()