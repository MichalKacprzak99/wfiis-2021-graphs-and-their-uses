import sys

sys.path.append('../..')

from grafy.project4.bellman_ford import generate_connected_digraph
from grafy.project4.johnson import johnson
from grafy.project1.graph_visualization import visualize_weighted_graph


def print_array(arr):
    """
    prints a 2-D numpy array in a nicer format
    """
    for a in arr:
        for elem in a:
            print(f"{elem:>2.0f}".rjust(5), end="")
        print(end="\n")


if __name__ == '__main__':
    vertices_amount = 7
    probability = 0.5

    adj_matrix, weighted_adj_matrix, graph_connected_components, cycle_info = generate_connected_digraph(vertices_amount,
                                                                                                         probability)

    print("Digraph with weights:")
    print_array(weighted_adj_matrix)

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
    print_array(D)

    visualize_weighted_graph(adj_matrix, weighted_adj_matrix, True)
