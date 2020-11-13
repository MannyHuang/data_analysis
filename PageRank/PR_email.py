import pandas as pd
import networkx as nx
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

emails = pd.read_csv('./input/Emails.csv')
file = pd.read_csv('./input/Aliases.csv')
aliases = {}
for index, row in file.iterrows():
  aliases[row['Alias']] = row['PersonId']

file = pd.read_csv('./input/Persons.csv')
persons = {}
for index, row in file.iterrows():
  persons[row['Id']] = row['Name']

def unify_name(name):
  name = str(name).lower()
  name = name.replace(',', '').split('@')[0]

  if name in aliases.keys():
    return persons[aliases[name]]
  return name

def show_graph(graph, layout='spring_layout'):
  if layout == 'circular_layout':
    positions = nx.circular_layout(graph)
  else:
    positions = nx.spring_layout(graph)

  nodesize = [x['pagerank']*2000 for v,x in graph.nodes(data=True)]

  edgesize = [np.sqrt(e[2]['weight']) for e in graph.edges(data=True)]

  nx.draw_networkx_nodes(graph, positions, node_size=nodesize, alpha=0.4)

  nx.draw_networkx_edges(graph, positions, edgelist=edgesize, alpha=0.2)

  nx.draw_networkx_labels(graph, positions, font_size=10)

  plt.show()

emails.MetadataFrom = emails.MetadataFrom.apply(unify_name)
emails.MetadataTo = emails.MetadataTo.apply(unify_name)

edges_weights_temp = defaultdict(list)
for row in zip(emails.MetadataFrom, emails.MetadataTo, emails.RawText):
  temp = (row[0], row[1])
  if temp not in edges_weights_temp:
    edges_weights_temp[temp] = 1
  else:
    edges_weights_temp[temp] += 1

edges_weights = [(key[0], key[1], val) for key, val in edges_weights_temp.items()]
graph = nx.DiGraph()
graph.add_weighted_edges_from(edges_weights)
pagerank = nx.pagerank(graph)
nx.set_node_attributes(graph, name='pagerank', values=pagerank)

show_graph(graph)

pagerank_threshold = 0.005

small_graph = graph.copy()

for n, p_rank in graph.nodes(data=True):
  if p_rank['pagerank'] < pagerank_threshold:
    small_graph.remove_node(n)

show_graph(small_graph, 'circular_layout')


  