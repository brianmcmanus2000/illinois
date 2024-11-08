import math
import random
import networkx as nx
import matplotlib.pyplot as plt

def ER_graph(n, p_func):
    """
    Create an Erdős-Réyni random graph
    
    Parameters:
    n (int): Number of nodes
    p_func: Either a float between 0 and 1, or a function that takes n as input and returns probability
    """
    # Create empty directed graph
    G = nx.Graph()
    
    # Add n nodes
    G.add_nodes_from(range(n))
    
    # Calculate probability if p_func is a function
    if callable(p_func):
        p = p_func(n)
    else:
        p = p_func
    
    # For each possible edge, add it with probability p
    for i in range(n):
        for j in range(i+1,n):
            if random.random() < p:
                G.add_edge(i, j)
    return G

# Example usage:
if __name__ == "__main__":
    def p_inverse_square(n):
        return 1/(n*n)
    
    def p_log_n(n):
        return math.log(n)/n
    
    def p_inverse(n):
        return 1/n
    
    # Create graphs with different probability functions
    n = 50
    G1 = ER_graph(n, p_inverse_square)
    G2 = ER_graph(n, p_log_n)
    G3 = ER_graph(n, p_inverse)
    n=150
    G4 = ER_graph(n, p_inverse_square)
    G5 = ER_graph(n, p_log_n)
    G6 = ER_graph(n, p_inverse)
    # Optional: visualize the graphs
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    nx.draw(G1, with_labels=True)
    plt.title("p = 1/n², n=50")
    
    plt.subplot(132)
    nx.draw(G2, with_labels=True)
    plt.title("p = log(n)/n, n=50")
    
    plt.subplot(133)
    nx.draw(G3, with_labels=True)
    plt.title("p = 1/n, n=50")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    nx.draw(G4, with_labels=True)
    plt.title("p = 1/n², n=150")
    
    plt.subplot(132)
    nx.draw(G5, with_labels=True)
    plt.title("p = log(n)/n, n=150")
    
    plt.subplot(133)
    nx.draw(G6, with_labels=True)
    plt.title("p = 1/n, n=150")
    
    plt.tight_layout()
    plt.show()