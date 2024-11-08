import networkx as nx
from networkx.algorithms import bipartite
import csv
import matplotlib.pyplot as plt

# test1
# Top 3 Hubs : 1,2,3
# Top 3 Authorities: 1,2,3
# test2
# Top 3 Hubs: 12,2100,387
# Top 3 Authorities: 10897,21443,38976

def create_graph_from_file(filename:str, offset:int):
    hubs = set()
    authorities = set()
    edges = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
        for _ in range(offset):
            next(spamreader, None)
        for row in spamreader:
            hubs.add("hub:"+str(row[0]))
            authorities.add("authority:"+str(row[1]))
            edges.append(("hub:"+str(row[0]),"authority:"+str(row[1])))
    G = nx.Graph()
    G.add_nodes_from(hubs,bipartite=0,weight=1)
    G.add_nodes_from(authorities,bipartite=1,weight=1)
    G.add_edges_from(edges)
    return G

def sum_of_neighbors(G, node):
    neighbors = list(G.neighbors(node))  # Convert iterator to list
    return sum(G.nodes[n]['weight'] for n in neighbors)

def normalize(G):
    hub_sum = sum(w['weight'] for n, w in G.nodes(data=True) if G.nodes[n]["bipartite"] == 0)
    authority_sum = sum(w['weight'] for n, w in G.nodes(data=True) if G.nodes[n]["bipartite"] == 1)
    
    hubs = [n for n, d in G.nodes(data=True) if d["bipartite"] == 0]
    authorities = [n for n, d in G.nodes(data=True) if d["bipartite"] == 1]
    
    for hub in hubs:
        G.nodes[hub]['weight'] /= hub_sum
    for authority in authorities:
        G.nodes[authority]['weight'] /= authority_sum

def run_hits_once(G):
    hubs = [(n, d['weight']) for n, d in G.nodes(data=True) if d["bipartite"] == 0]
    authorities = [(n, d['weight']) for n, d in G.nodes(data=True) if d["bipartite"] == 1]
    
    # Use node[0] to get just the node name from the (node, weight) tuple
    for authority, _ in authorities:  # Changed to unpack tuple
        increment = sum_of_neighbors(G, authority)
        G.nodes[authority]['weight'] += increment
        
    for hub, _ in hubs:  # Changed to unpack tuple
        increment = sum_of_neighbors(G, hub)
        G.nodes[hub]['weight'] += increment
    
    normalize(G)
def run_hits_k_times(G, k):
    for _ in range(k):
        run_hits_once(G)
    
def print_weights(G):
    for node in G.nodes:
        print(str(node) + "weight: " +str(G.nodes[node]['weight']))

def get_highest_auths(G):
    # Get all authority nodes with their weights
    authorities = [(n, d['weight']) for n, d in G.nodes(data=True) if d["bipartite"] == 1]
    # Sort by weight in descending order and take top 3
    sorted_auths = sorted(authorities, key=lambda x: x[1], reverse=True)
    return [node for node, _ in sorted_auths[:3]]

def get_highest_hubs(G):
    # Get all hub nodes with their weights
    hubs = [(n, d['weight']) for n, d in G.nodes(data=True) if d["bipartite"] == 0]
    # Sort by weight in descending order and take top 3
    sorted_hubs = sorted(hubs, key=lambda x: x[1], reverse=True)
    return [node for node, _ in sorted_hubs[:3]]

G = create_graph_from_file("HITS_input2.txt",1)
run_hits_k_times(G,10)  
best_auths = get_highest_auths(G)
best_hubs = get_highest_hubs(G)
print(best_hubs)
print(best_auths)
hubs = [(n, d['weight']) for n, d in G.nodes(data=True) if d["bipartite"] == 0]
# nx.draw_networkx(G, pos=nx.drawing.layout.bipartite_layout(G, [n for n, _ in hubs]))
# plt.show()