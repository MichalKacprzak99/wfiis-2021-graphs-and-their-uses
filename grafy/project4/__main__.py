import sys

sys.path.append('../..')

from grafy.project4.kosaraju import kosaraju
from grafy.project4.bellman_ford import bellman_ford, assign_weights_to_adj_matrix, generate_connected_digraph
from grafy.project4.digraph_generation import generate_N_P_digraph
from grafy.project4.johnson import johnson



vertice_amount = 7
probability = 0.5

adj_matrix, weighted_adj_matrix, graph_connected_components, cycle_info = generate_connected_digraph(vertice_amount,
                                                                                                     probability)

print("Digraph with weights:")
print(weighted_adj_matrix)

print(" ")
print(graph_connected_components)
print("Graph has one connected component")


print(" ")
print("Bellman Ford algorithm:")
print("No negative cycles found: ", cycle_info[0])
print("Array of shortest paths:")
print(cycle_info[1])
print()
print("Array of previous nodes in shortest paths:")
print(cycle_info[2])


print(" ")
print("Johnson algorithm:")
print("Distance matrix:")
D = johnson(adj_matrix, weighted_adj_matrix)
for row in D:
    print(row)

visualize_weighted_graph(adj_matrix, weighted_adj_matrix, True)
