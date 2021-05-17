import sys

sys.path.append('..')

from grafy.project1.graph_conversion import adj_matrix_to_list
from grafy.project2.check_if_euler import get_euler_graph, print_euler_cycle
from grafy.project2.check_if_hamiltonian import check_graph, sample_adj_list
from grafy.project2.degree_sequence import degree_sequence_checker
from grafy.project2.graph_components import find_biggest_graph_component
from grafy.project2.graph_randomization import generate_regular_graph

check_graph(sample_adj_list)
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

find_biggest_graph_component(adj_list)

print_euler_cycle(get_euler_graph(5))
generate_regular_graph(7, 2)