from graph_generation import generate_N_P_graph, generate_N_L_graph
from graph_visualization import visualize_graph
from graph_conversion import *


adj_matrix = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
             [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]


if __name__ == "__main__":

    adj_list = adj_matrix_to_list(adj_matrix)
    print_adj_list(adj_list)
    converted_adj_matrix_from_adj_list = adj_list_to_matrix(adj_list)
    print(np.array_equal(np.asarray(adj_matrix), converted_adj_matrix_from_adj_list))

    inc_matrix = adj_matrix_to_inc_matrix(adj_matrix)
    print(inc_matrix)
    converted_adj_matrix_from_inc_matrix = inc_matrix_to_adj_matrix(inc_matrix)
    print(np.array_equal(np.asarray(adj_matrix), converted_adj_matrix_from_inc_matrix))

    # visualize_graph(generate_N_L_graph(10, 15))