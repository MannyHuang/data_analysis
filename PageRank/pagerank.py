import networkx as nx

# setting oriented graph
G = nx.DiGraph()

# relation of edges
edges = [('A','B'), ('A','C'),('A','D'),('B','A'),('B','D'), ('C','A'), ('D','B'),('D','C')]
for edge in edges:
  G.add_edge(edge[0], edge[1])
pagerank_list = nx.pagerank(G, alpha=1)
print('pagerank is ', pagerank_list)