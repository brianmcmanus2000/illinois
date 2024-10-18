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
            node_list.append((row[0],{'preferences':row[1:None]}))
    return node_list

def get_initial_prices():
    prices = []
    for i in range(100):
        prices.append((i,{'price':0}))
    return prices

def get_prices(G):
    prices = []
    houses = list(G.nodes.data())[0:100:None]
    for house in houses:
        prices.append(int(house[1]['price']))
    return prices

def create_pref_seller_graph(G):
    nodes = list(G.nodes(data=True))
    houses = nodes[0:100]
    buyers = nodes[100:None]
    prices = get_prices(G)
    for buyer in buyers:
        preferences = list(map(int,(buyer[1]['preferences'])))       
        matches = maxelements([x - y for x, y in zip(preferences, prices)])
        for match in matches:
            G.add_edge(buyer[0],houses[match][0])


def auction(G):
    houses = list(G.nodes.data())[0:100:None]
    create_pref_seller_graph(G)
    max_matching = nx.max_weight_matching(G,maxcardinality=True)
    if not nx.is_perfect_matching(G,max_matching):    
        for edge in max_matching:
            if isinstance(edge[1], int):
                house = edge[1]
            else:
                house = edge[0]
            houses[house][1]['price']+=1
        min_price = min(get_prices(G))
        if min_price > 0:
            for house in houses:
                house[1]['price']-=min_price
        G.remove_edges_from(list(G.edges()))
        return auction(G)
    else:
        G.remove_edges_from(list(G.edges()))
        G.add_edges_from(max_matching)
        return max_matching

G = nx.Graph()
buyers = get_preferences()
houses = get_initial_prices()
G.add_nodes_from(houses,bipartite=0)
G.add_nodes_from(buyers,bipartite=1)
max_matching = auction(G)
with open('market-clearing.csv', 'w', newline='') as csvfile:
    nodes = list(G.nodes(data=True))
    houses = nodes[0:100]
    buyers = nodes[100:None]
    buyers_preferences = []
    for buyer in buyers:
        buyers_preferences.append(list(map(int,(buyer[1]['preferences']))))
    spamwriter = csv.writer(csvfile)
    for edge in max_matching:
        if isinstance(edge[0], int):
            correct_order = (edge[1],edge[0])
        else:
            correct_order = (edge[0],edge[1])
        price = houses[correct_order[1]][1]['price']
        print(buyers_preferences[correct_order[1]])
        valuation = buyers_preferences[correct_order[1]]
        payoff = valuation-price
        spamwriter.writerow([correct_order[0],"house"+correct_order[1],str(payoff)])