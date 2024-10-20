import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import csv
from collections import deque

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

def find_constricted_set(G, matching):
    nodes = list(G.nodes(data=False))
    houses = nodes[0:100]
    buyers = nodes[100:None]
    matched_nodes = set([n for pair in matching for n in pair])
    matched_X = [n for n in buyers if n in matched_nodes]
    matched_Y = [n for n in houses if n in matched_nodes]
    unmatched_X = [n for n in buyers if n not in matched_X]
    reachable_X = set(unmatched_X)
    reachable_Y = set()
    queue = deque(unmatched_X)
    visited_X = set(unmatched_X)
    visited_Y = set()
    while queue:
        current = queue.popleft()
        for neighbor in set(G.neighbors(current)):
            if neighbor not in visited_Y:
                reachable_Y.add(neighbor)
                visited_Y.add(neighbor)
                if neighbor in matched_Y:
                    for (first,second) in matching:
                        if (first == neighbor):
                            matched_partner = second
                        elif (second == neighbor):
                            matched_partner = first
                    if matched_partner not in visited_X:
                        reachable_X.add(matched_partner)
                        visited_X.add(matched_partner)
                        queue.append(matched_partner)
    if len(reachable_Y) < len(reachable_X):
        return list(reachable_Y)
    else:
        return None
    
def calculate_potential(G,potential_list):
    prices = get_prices(G)
    nodes = list(G.nodes(data=True))
    buyers = nodes[100:None]
    buyer_potential = 0
    for buyer in buyers:
        preferences = list(map(int,(buyer[1]['preferences'])))       
        buyer_potential += max([x - y for x, y in zip(preferences, prices)])
    potential_list.append(sum(prices)+buyer_potential)
    return potential_list

def auction(G,potential_list):
    houses = list(G.nodes.data())[0:100:None]
    create_pref_seller_graph(G)
    calculate_potential(G,potential_list)
    max_matching = nx.max_weight_matching(G,maxcardinality=True)
    if not nx.is_perfect_matching(G,max_matching):
        constricted_set = find_constricted_set(G,max_matching)
        for house in constricted_set:
            houses[house][1]['price']+=1
        min_price = min(get_prices(G))
        if min_price > 0:
            for house in houses:
                house[1]['price']-=min_price
        G.remove_edges_from(list(G.edges()))
        return auction(G,potential_list)
    else:
        G.remove_edges_from(list(G.edges()))
        G.add_edges_from(max_matching)
        return max_matching
    
def write_csv(G,max_matching):
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
            buyer_num = int(correct_order[0][5:None])
            valuation = buyers_preferences[buyer_num][correct_order[1]]
            payoff = int(valuation)-(price)
            spamwriter.writerow([correct_order[0],"house"+str(correct_order[1]),str(payoff)])
            
G = nx.Graph()
buyers = get_preferences()
houses = get_initial_prices()
G.add_nodes_from(houses,bipartite=0)
G.add_nodes_from(buyers,bipartite=1)
potential_list=[]
max_matching = auction(G,potential_list)
write_csv(G,max_matching)
plt.plot(range(len(potential_list)),potential_list)
plt.show()
