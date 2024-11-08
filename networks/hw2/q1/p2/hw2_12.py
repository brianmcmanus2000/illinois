import networkx as nx
import csv

def create_graph_from_file(filename:str, offset:int):
    edges = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar='"')
        for _ in range(offset):
            next(spamreader, None)
        for row in spamreader:
            edges.append((row[0],row[1]))
    G = nx.DiGraph()
    G.add_edges_from(edges)
    norm = 1.0 / G.number_of_nodes()
    for node in G.nodes():
        G.nodes[node]['weight'] = norm
    return G

def basic_pagerank(G, num_iterations, tolerance=1e-18):
    N = G.number_of_nodes()
    for node in G.nodes():
        G.nodes[node]['weight'] = 1.0/N
    
    for n in range(num_iterations):
        old_weights = {node: G.nodes[node]['weight'] for node in G.nodes()}
        max_diff = 0  # Track maximum change in any node's weight
        
        for node in G.nodes():
            incoming = G.predecessors(node)
            try:
                rank_sum = sum(old_weights[in_node] / G.out_degree(in_node) 
                              for in_node in incoming)
            except ZeroDivisionError:
                rank_sum = 0
            
            G.nodes[node]['weight'] = rank_sum
            # Update max difference
            max_diff = max(max_diff, abs(G.nodes[node]['weight'] - old_weights[node]))
        
        # Check for convergence
        if max_diff < tolerance:
            print("stopped early in basic_pageranks at step "+str(n))
            break
            
    return G

def scaled_basic_pagerank(G, num_iterations, d=0.85, tolerance=1e-18):
    N = G.number_of_nodes()
    for node in G.nodes():
        G.nodes[node]['weight'] = 1.0/N
    
    for n in range(num_iterations):
        old_weights = {node: G.nodes[node]['weight'] for node in G.nodes()}
        max_diff = 0  # Track maximum change in any node's weight
        
        for node in G.nodes():
            incoming = G.predecessors(node)
            rank_sum = sum(old_weights[in_node] / G.out_degree(in_node) 
                          for in_node in incoming)
            G.nodes[node]['weight'] = (1-d)/N + d * rank_sum
            
            # Update max difference
            max_diff = max(max_diff, abs(G.nodes[node]['weight'] - old_weights[node]))
        
        # Check for convergence
        if max_diff < tolerance:
            print("stopped early in scaled_basic_pagerank at step "+str(n))
            break
            
    return G

G = create_graph_from_file("data.txt", 0)
G = basic_pagerank(G, 100)
sorted_nodes = sorted(G.nodes(data=True), key=lambda x: int(x[0]))

with open('basic_pagerank.txt', 'w') as f:
    for node, data in sorted_nodes:
        f.write(f"{node}: {data['weight']}\n")

G = create_graph_from_file("data.txt", 0)
G = scaled_basic_pagerank(G, 100)
sorted_nodes = sorted(G.nodes(data=True), key=lambda x: int(x[0])) 

with open('scaled_pagerank.txt', 'w') as f:
    for node, data in sorted_nodes:
        f.write(f"{node}: {data['weight']}\n")
