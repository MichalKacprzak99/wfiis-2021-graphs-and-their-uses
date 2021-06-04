import sys

sys.path.append('../..')

from grafy.project4.kosaraju import kosaraju
from grafy.project4.bellman_ford import bellman_ford, assign_weights_to_adj_matrix
from grafy.project4.digraph_generation import generate_N_P_digraph
from grafy.project4.johnson import johnson
from grafy.project1.graph_visualization import visualize_graph

vertice_number = 7
probability = 0.5

adj_matrix = generate_N_P_digraph(vertice_number, probability)
graph_connected_components = kosaraju(adj_matrix)

weighted_adj_matrix = assign_weights_to_adj_matrix(adj_matrix)
cycle_info = bellman_ford(adj_matrix, weighted_adj_matrix, 0)
counter = 1

while len(graph_connected_components) != 1 or cycle_info[0] is not True:
    adj_matrix = generate_N_P_digraph(vertice_number, probability)
    graph_connected_components = kosaraju(adj_matrix)

    weighted_adj_matrix = assign_weights_to_adj_matrix(adj_matrix)
    cycle_info = bellman_ford(adj_matrix, weighted_adj_matrix, 0)
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
D = johnson(adj_matrix, weighted_adj_matrix)
for row in D:
    print(row)

visualize_graph(weighted_adj_matrix, True, True)
