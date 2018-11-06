from bs4 import BeautifulSoup
import pickle
import os
import networkx as nx

class Rich():
    """Rich class for forbes"""

    def __init__(self, name, worth, rank,age, source, country):
        self.name = name
        self.worth = worth
        self.rank = rank
        self.age = age
        self.source = source
        self.country = country

    def __str__(self):
        return str(self.rank + " -- " + self.name + " " + str(self.worth) + " --> " + str(self.source))


with open('forbes.html', 'r') as _file:
    file = _file.read()
    soup = BeautifulSoup(file, "html")
    peoples = soup.findAll("tr", class_="data")

    richs = list()
    for people in peoples:
        colums = people.findAll("td")
        counter = 0
        for colum in colums:
            if counter == 0:
                pass
            elif counter == 1:
                rank = colum.text.replace("#","")
            elif counter == 2:
                name = colum.text
            elif counter == 3:
                worth = float(colum.text.split(" ")[0][1:])
            elif counter == 4:
                age = colum.text.replace(" ", "")
            elif counter == 5:
                source = [text.strip().lower() for text in colum.text.split(",")]
            elif counter == 6:
                country = colum.text
            counter += 1
        richs.append(Rich(name, worth, rank, age, source, country))

    for rich in richs:
        pass
        #print(rich)

def get_edges(richs):
    partions = dict()

    for rich in richs:
        for src in rich.source:
            if not partions.get(src):
                partions[src] = list()
                partions[src].append(rich.name)
            else:
                partions[src].append(rich.name)

    return partions

def edge_to_tuple(richs_edges):
    edge_tuple_list = list()
    for key, value in richs_edges.items():
        for edge in value:
            for connect_edge in value:
                if not edge == connect_edge:
                    edge_tuple_list.append((edge, connect_edge))
    return edge_tuple_list

def get_nodes(richs):
    nodes = list()
    for rich in richs:
        nodes.append(rich.name)
    return nodes

# for rich in richs:
#     print(rich)


# nodes = get_nodes(richs)
rich_edges = get_edges(richs)
rich_edges_tuple = edge_to_tuple(rich_edges)

G = nx.Graph()

for rich in richs:
    G.add_node(rich.name, worth=rich.worth, age=rich.age, rank=rich.rank, country=rich.country)

G.add_edges_from(rich_edges_tuple)

print(G.number_of_nodes())
print(G.number_of_edges())

nx.write_gexf(G, "forbes.gexf")
# for edge in rich_edges_tuple:
#     print(edge)
# for key, value in rich_edges.items():
#     print(key + " --> " + str(value))