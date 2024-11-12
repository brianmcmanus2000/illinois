import networkx as nx
from collections import defaultdict

def calculate_modularity(G, communities):
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

def calculate_edge_betweenness(G):
    edge_betweenness = defaultdict(float)
    
    for s in G.nodes():
        paths = nx.single_source_shortest_path(G, s)
        edge_contributions = defaultdict(float)
        for t in paths:
            if s == t:
                continue
            path = paths[t]
            for i in range(len(path) - 1):
                edge = tuple(sorted([path[i], path[i + 1]]))
                edge_contributions[edge] += 1
        for edge, contribution in edge_contributions.items():
            edge_betweenness[edge] += contribution
    return dict(edge_betweenness)

def find_communities(G, target_communities):
    working_graph = G.copy()
    
    removed_edges = []
    current_communities = 1
    i=0
    while True:
        
        communities = list(nx.connected_components(working_graph))
        num_communities = len(communities)
        if (num_communities !=current_communities):
            modularity = calculate_modularity(G, communities)
            print(f"\nNumber of communities: {current_communities}")
            print(f"Modularity: {modularity}")
            print("Number of edges removed:", len(removed_edges))
            current_communities = num_communities
        if num_communities >= target_communities:
            break

        edge_betweenness = calculate_edge_betweenness(working_graph)
        if not edge_betweenness:
            break
            
        max_edge = max(edge_betweenness.items(), key=lambda x: x[1])[0]
        
        working_graph.remove_edge(*max_edge)
        removed_edges.append(max_edge)
        i+=1
        print(f"removed edge: {max_edge}, total edges removed: {i}",end='\r')
    return list(communities), removed_edges

def analyze_graph(file_path):
    """
    Analyze graph from edge list file
    """
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            edge = line.strip().strip('()').split(',')
            x, y = int(edge[0]), int(edge[1])
            G.add_edge(x, y)
    initial_communities = [set(G.nodes())]
    initial_modularity = calculate_modularity(G, initial_communities)
    print(G)
    print(f"Initial modularity: {initial_modularity}")

    n_communities = 5
    communities, removed_edges = find_communities(G, n_communities)
    modularity = calculate_modularity(G, communities)
    
    print(f"\nNumber of communities: {n_communities}")
    print(f"Modularity: {modularity}")
    print("Number of edges removed:", len(removed_edges))

# Example usage
if __name__ == "__main__":
    graph_file = "WattsStrogatz.txt"
    analyze_graph(graph_file)