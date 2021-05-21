import sys
sys.path.append('../..')

from grafy.project1.graph_conversion import adj_matrix_to_list
from grafy.project2.check_if_euler import get_euler_graph, print_euler_cycle
from grafy.project2.check_if_hamiltonian import check_graph, sample_adj_list
from grafy.project2.degree_sequence import degree_sequence_checker
from grafy.project2.graph_components import find_biggest_graph_component
from grafy.project2.graph_randomization import generate_regular_graph
from grafy.project1.graph_visualization import visualize_graph


if __name__ == "__main__":
    print("Check if hamilton cycle")
    check_graph(sample_adj_list)

    print("Check degree sequence")
    exampleCorrectFromLecture = [4, 2, 3, 2, 3, 2]
    print(degree_sequence_checker(exampleCorrectFromLecture))

    graph_N_L = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 ]

    adj_list = adj_matrix_to_list(graph_N_L)
    print("Find biggest graph component")
    find_biggest_graph_component(adj_list)

    print("Find and print Euler cycle")
    print_euler_cycle(get_euler_graph(5))

    print("Generate regular graph")
    regular_graph = generate_regular_graph(8, 3)
    visualize_graph(regular_graph)
