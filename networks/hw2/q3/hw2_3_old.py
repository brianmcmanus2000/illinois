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
    #no need to normalize because we only care about which edge is maximal
    return dict(betweenness)
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
            f = open("output.txt","a")
            f.write("Number of communities: "+str(num_communities)+", ")
            f.write("Modularity: "+str(modularity)+", ")
            f.write("Number of edges removed: " + str(len(removed_edges))+"\n")
            f.close()
            current_communities = num_communities
        if num_communities >= target_communities:
            break
        # edge_betweenness = nx.edge_betweenness_centrality(working_graph)
        edge_betweenness = calculate_edge_betweenness(working_graph)
        if not edge_betweenness:
            break
        max_edge = max(edge_betweenness.items(), key=lambda x: x[1])[0]
        working_graph.remove_edge(*max_edge)
        removed_edges.append(max_edge)
        i+=1
        print(f"removed edge: {max_edge}, total edges removed: {i}, number of communities: {num_communities}     ",end='\r')
    return list(communities), removed_edges

def analyze_graph(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            edge = line.strip().strip('()').split(',')
            x, y = int(edge[0]), int(edge[1])
            G.add_edge(x, y)
    initial_communities = [set(G.nodes())]
    initial_modularity = calculate_modularity(G, initial_communities)
    f = open("output.txt","w")
    f.write("Number of communities: 1, Modularity: "+str(initial_modularity)+", Number of edges removed: 0\n")
    f.close()
    n_communities = 5
    communities, removed_edges = find_communities(G, n_communities)
    modularity = calculate_modularity(G, communities)
    
    print()
    print(f"Number of communities: {n_communities}")
    print(f"Modularity: {modularity}")
    print("Number of edges removed:", len(removed_edges))

if __name__ == "__main__":
    graph_file = "ErdosRenyi.txt"
    analyze_graph(graph_file)        