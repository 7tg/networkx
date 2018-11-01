import pickle
import networkx as nx
import matplotlib.pyplot as plt

with open('graph.dat', 'rb') as file:
    G = pickle.loads(file.read())

print(G.number_of_nodes())

# def plot_network(G):
#    pos = nx.spring_layout(G)
#    plt.figure(figsize=(10,10))
#    nx.draw_networkx(G, pos, iterations=20, node_grouping='bipartite',
#    with_labels=False, node_size = 5)

fig, axs = plt.subplots(1,1, figsize=(25,25))

# Define node positions using layout algo
# pos = nx.spring_layout(G, center=(1,1), k=40, iterations=5) # returns error
pos = nx.circular_layout(G)

# draw
nx.draw(G,axis=axs, pos=pos, node_size=1)
plt.draw()
