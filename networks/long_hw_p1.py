import networkx as nx
import matplotlib.pyplot as plt
import random    
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
def calculate_update(G,steps_per_unit):
    for (u,v,w) in G.edges(data=True):
        neighbors = nx.common_neighbors(G,u,v)
        for common_neighbor in neighbors:
            w['update']+=G.get_edge_data(common_neighbor,u)['weight']/steps_per_unit*G.get_edge_data(common_neighbor,v)['weight']/steps_per_unit
            
def update_nodes(G):
    for (u,v,w) in G.edges(data=True):
        w['weight'] += w['update']
        w['history'].append(w['weight'])
        w['update']=0

def generate_graph(n,lower,upper):
    G = nx.complete_graph(n)
    for (u,v,w) in G.edges(data=True):
        w['weight']  = random.uniform(lower,upper)
        w['update']  = 0 
        w['history'] = [w['weight']]
    return G
def run_updates(G,units,steps_per_unit):
    for i in range(0,int(units*steps_per_unit)):
        calculate_update(G,steps_per_unit)
        update_nodes(G)

def smooth_draw(G,units,steps_per_unit):
    x_axis = np.linspace(0,units,int(units*steps_per_unit+1))
    edge_signs=[0,0]
    for (u,v,w) in G.edges(data=True):
        xnew = np.linspace(0, units, 300) 
        spl = make_interp_spline(x_axis, w['history'], k=2) 
        power_smooth = spl(xnew)
        if w['weight'] > 0:
            plt.plot(xnew, power_smooth,'b')
            edge_signs[0]+=1
        else:
            plt.plot(xnew, power_smooth,'r')
            edge_signs[1]+=1
    return edge_signs

def rough_draw(G,units,steps_per_unit):
    x_axis = np.linspace(0,units,int(units*steps_per_unit+1))
    edge_signs=[0,0]
    for (u,v,w) in G.edges(data=True):
        if w['weight'] > 0:
            plt.plot(x_axis,w['history'],'b')
            edge_signs[0]+=1
        else:
            plt.plot(x_axis,w['history'],'r')
            edge_signs[1]+=1
    return edge_signs

G = generate_graph(100,-0.5,0.5)
steps_per_unit = 20
units = 4.1
run_updates(G,units,steps_per_unit)
edge_signs = smooth_draw(G,units,steps_per_unit)
print(edge_signs)
plt.yticks(fontsize=30)
plt.xticks(fontsize=30)
plt.show()