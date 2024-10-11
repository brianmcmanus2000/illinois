import networkx as nx
import matplotlib.pyplot as plt
import random    
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
def calculate_update(G):
    for (u,v,w) in G.edges(data=True):
        neighbors = nx.common_neighbors(G,u,v)
        for common_neighbor in neighbors:
            w['update']+=G.get_edge_data(common_neighbor,u)['weight']*G.get_edge_data(common_neighbor,v)['weight']
            
def update_nodes(G):
    for (u,v,w) in G.edges(data=True):
        w['weight'] += w['update']
        w['history'].append(w['weight'])
        w['update']=0

def generate_graph(n):
    G = nx.complete_graph(n)
    for (u,v,w) in G.edges(data=True):
        w['weight']  = random.uniform(-0.75,0.75)
        w['update']  = 0 
        w['history'] = [w['weight']]
    return G
def run_n_updates(n,G):
    for i in range(0,n):
        calculate_update(G)
        update_nodes(G)

def smooth_draw(G,num_updates):
    x_axis = list(range(0,num_updates))
    for (u,v,w) in G.edges(data=True):
        xnew = np.linspace(0, num_updates, 300) 
        spl = make_interp_spline(x_axis, w['history'], k=2)  # type: BSpline
        power_smooth = spl(xnew)
        if w['weight'] > 0:
            plt.plot(xnew, power_smooth,'b')
        else:
            plt.plot(xnew, power_smooth,'r')

def rough_draw(G,num_updates):
    x_axis = list(range(0,num_updates))
    for (u,v,w) in G.edges(data=True):
        if w['weight'] > 0:
            plt.plot(x_axis,w['history'],'b')
        else:
            plt.plot(x_axis,w['history'],'r')

G = generate_graph(100)
run_n_updates(2,G)
num_updates = len(G.get_edge_data(0,1)['history'])
smooth_draw(G,num_updates)
#rough_draw(G,num_updates)
#pos=nx.spring_layout(G)
#nx.draw_networkx_edge_labels(G,pos, font_color='b',font_size=14, verticalalignment="center_baseline")
#nx.draw_networkx(G,pos)

plt.show()