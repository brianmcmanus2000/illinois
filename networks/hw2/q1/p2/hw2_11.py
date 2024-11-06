import networkx as nx

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

