import kosaraju
from project3 import connected_graph_generation
import bellman_ford
from numpy import all

adj_matrix = connected_graph_generation.generate_connected_graph(7)
graph_connected_components = kosaraju.kosaraju(adj_matrix)
print(graph_connected_components)
if all(graph_connected_components == 1):
    print("Graph has one connected component!")

print(adj_matrix)
bellman_ford.bellman_ford(adj_matrix, 0)
