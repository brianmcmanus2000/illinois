import networkx as nx, igraph as ig
from collections import defaultdict
import time

def calculate_modularity(G, communities):
    # I know we can use the library method for this function 
    # but I already wrote my own implementation
    m = G.number_of_edges()
    if m == 0:
        return 0
    Q = 0
    degrees = dict(G.degree())
    for community in communities:
        for i in community:
            for j in community:
                if G.has_edge(i, j):
                    Aij = 1
                else:
                    Aij = 0
                kikj = degrees[i] * degrees[j] / (2 * m)
                Q += (Aij - kikj)
    return Q / (2 * m)

def find_communities(G, target_communities):
    working_graph = G.copy()
    removed_edges = []
    current_communities = 1
    edges_removed_count=0
    while True:
        communities = list(nx.connected_components(working_graph))
        num_communities = len(communities)
        # Logic to see if removing the last edge increased the number of communities
        # If it did then we write the output for the file
        if (num_communities !=current_communities):
            modularity = calculate_modularity(G, communities)
            f = open("output.txt","a")
            f.write("Number of communities: "+str(num_communities)+", ")
            f.write("Modularity: "+str(modularity)+", ")
            f.write("Number of edges removed: " + str(len(removed_edges))+"\n")
            f.close()
            current_communities = num_communities
        if num_communities >= target_communities:
            break
        # For some reason the igraph implementation is orders of magnitude faster 
        # than the networkx implementation, so I convert to igraph only for this part
        # Borrowed from stack overflow at 
        # https://stackoverflow.com/questions/23235964/interface-between-networkx-and-igraph
        g = ig.Graph(len(working_graph), list(zip(*list(zip(*nx.to_edgelist(working_graph)))[:2])))
        betweenness_values  = ig.GraphBase.edge_betweenness(g)
        edge_betweenness = {edge.tuple: betweenness for edge, betweenness in zip(g.es, betweenness_values)}
        if not edge_betweenness:
            break
        max_edge = max(edge_betweenness.items(), key=lambda x: x[1])[0]
        working_graph.remove_edge(*max_edge)
        removed_edges.append(max_edge)
        edges_removed_count+=1
        # Print the most recent removed edge. Overwrites the line instead of printing a newline
        print(f"removed edge: {max_edge}, total edges removed: {edges_removed_count}, number of communities: {num_communities}     ",end='\r')
    return list(communities), removed_edges

def analyze_graph(file_path):
    G = nx.Graph()
    # Reading input file
    with open(file_path, 'r') as f:
        for line in f:
            edge = line.strip().strip('()').split(',')
            x, y = int(edge[0]), int(edge[1])
            G.add_edge(x, y)
    initial_communities = [set(G.nodes())]
    initial_modularity = calculate_modularity(G, initial_communities)
    # Get the baseline information and write it to output file
    f = open("output.txt","w")
    f.write("Number of communities: 1, Modularity: "+str(initial_modularity)+", Number of edges removed: 0\n")
    f.close()
    n_communities = 5
    communities, removed_edges = find_communities(G, n_communities)
    modularity = calculate_modularity(G, communities)
    # Final print after 5 communities have been found
    print()
    print(f"Number of communities: {n_communities}")
    print(f"Modularity: {modularity}")
    print("Number of edges removed:", len(removed_edges))

if __name__ == "__main__":
    # Timing code
    t0 = time.time()
    graph_file = "Barabasi.txt"
    analyze_graph(graph_file)
    t1 = time.time()
    print(f"total time: {t1-t0}")