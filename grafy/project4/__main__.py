import sys
from numpy import all

sys.path.append('../..')

from grafy.project4 import kosaraju
from grafy.project4 import bellman_ford
from grafy.project4 import digraph_generation
from grafy.project4 import johnson
from grafy.project1 import graph_visualization

adj_matrix = digraph_generation.generate_N_P_digraph(7, 0.5)
graph_connected_components = kosaraju.kosaraju(adj_matrix)

weighted_adj_matrix = bellman_ford.assign_weights_to_adj_matrix(adj_matrix)
cycle_info = bellman_ford.bellman_ford(adj_matrix, weighted_adj_matrix, 0)
counter = 1

while all(graph_connected_components == 1) != 1 or cycle_info[0] is not True:
    adj_matrix = digraph_generation.generate_N_P_digraph(7, 0.5)
    graph_connected_components = kosaraju.kosaraju(adj_matrix)

    weighted_adj_matrix = bellman_ford.assign_weights_to_adj_matrix(adj_matrix)
    cycle_info = bellman_ford.bellman_ford(adj_matrix, weighted_adj_matrix, 0)
    counter = counter + 1

print("Generated digraph:")
print(adj_matrix)

print("Digraph with weights:")
print(weighted_adj_matrix)

print(" ")
print(graph_connected_components)
print("Graph has one connected component")
print("...after", counter, "tries.")

print(" ")
print("Bellman Ford algorithm:")
print(cycle_info)

print(" ")
print("Johnson algorithm:")
print("Distance matrix:")
D = johnson.johnson(adj_matrix, weighted_adj_matrix)
for row in D:
    print(row)
graph_visualization.visualize_graph(weighted_adj_matrix, True, True)

