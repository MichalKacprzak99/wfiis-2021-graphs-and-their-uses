import sys
sys.path.append('..')
from graph_generation import generate_N_P_graph, generate_N_L_graph
from graph_visualization import visualize_graph
from graph_conversion import *

if __name__ == "__main__":
    adj_matrix = generate_N_L_graph(15, 10)

    print("Adjacency matrix")
    print(adj_matrix)
    print()
    print("Adjacency list")
    print_adj_list(adj_matrix_to_list(adj_matrix))
    print()
    print("Incidence matrix")
    print(adj_matrix_to_inc_matrix(adj_matrix))
    visualize_graph(adj_matrix)

