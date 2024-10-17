import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import random    
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import csv

def maxelements(seq):
    max_indices = []
    if seq:
        max_val = seq[0]
        for i,val in ((i,val) for i,val in enumerate(seq) if val >= max_val):
            if val == max_val:
                max_indices.append(i)
            else:
                max_val = val
                max_indices = [i]
    return max_indices

def get_preferences():
    node_list = []
    with open('preference.csv', newline='') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')

        for row in spamreader:
            node_list.append((row[0],{'preferences':row[1:-1]}))
    return node_list

def get_initial_prices():
    prices = []
    for i in range(100):
        prices.append(("house"+str(i),{'price':0}))
    return prices

def create_pref_seller_graph(G,buyers,houses):
    for buyer in buyers:
        preferences = buyer[1]['preferences']
        matches = maxelements(preferences)
        for match in matches:
            G.add_edge(buyer[0],houses[match][0])


buyers = get_preferences()
houses = get_initial_prices()
G = nx.Graph()
G.add_nodes_from(houses,bipartite=0)
G.add_nodes_from(buyers,bipartite=1)
create_pref_seller_graph(G,buyers,houses)

nx.draw(G)
plt.show()