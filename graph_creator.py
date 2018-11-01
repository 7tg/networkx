from imdb import IMDb
import pickle
import os
import networkx as nx

def get_nodes(file_path):
    nodes = list()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            nodes.append(line.strip())
    return nodes

def get_edges(folder_path):
    edges = dict()
    movie_files = os.listdir(folder_path)
    for file_path in movie_files:
        if file_path.endswith('.txt'):
            edge_list = list()
            with open(folder_path + file_path, 'r', encoding='utf-8') as file:
                for actor in file:
                    edge_list.append(actor.strip())
            edges[file_path.split('_')[0]] = edge_list
    return edges

def edge_to_tuple(edge_list):
    edge_tuple_list = list()
    for edge in edge_list:
        for connect_edge in edge_list:
            if not edge == connect_edge:
                edge_tuple_list.append((edge, connect_edge))
    return edge_tuple_list

# Getting nodes
nodes = get_nodes('all_actors.txt')

# Getting edges
edges = get_edges('movies/')
# print(edges['0111161'])

# Formatting edges to tuple
edge_tuple = edge_to_tuple(edges['0111161'])
# print(edge_tuple)

G = nx.Graph()

G.add_nodes_from(nodes)

for movie,edge_list in edges.items():
    G.add_edges_from(edge_to_tuple(edge_list), label=movie)

print(G.number_of_nodes())
print(G.number_of_edges())

with open('graph.dat', 'wb') as file:
    file.write(pickle.dumps(G))
