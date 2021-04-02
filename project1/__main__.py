from graph_generation import generate_N_P_graph, generate_N_L_graph
from graph_visualization import visualize_graph
from graph_conversion import *

if __name__ == "__main__":
    adj_matrix = generate_N_L_graph(1, 0)

    print("Macierz sąsiedzctwa")
    print(adj_matrix)
    print("Lista sąsiedzctwa")
    print_adj_list(adj_matrix_to_list(adj_matrix))
    print("Macierz incydencji")
    print(adj_matrix_to_inc_matrix(adj_matrix))
    visualize_graph(adj_matrix)

    visualize_graph(generate_N_P_graph(10, 0.5))