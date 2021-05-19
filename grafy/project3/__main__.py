import sys

import numpy as np

sys.path.append('..')

from connected_graph_generation import generate_connected_graph
from dijkstra_algorithm import print_dijkstra_algorithm_result, dijkstra_algorithm
from grafy.project1.graph_visualization import visualize_graph
from graph_center import find_graph_centers, find_graph_minimax_centers, generate_vertices_distance_matrix
from kruskal_mst import kruskal_mst, print_tree


def print_array(arr):
    """
    prints a 2-D numpy array in a nicer format
    """
    for a in arr:
        for elem in a:
            print(f"{elem:<2.0f}".rjust(3), end="")
        print(end="\n")


if __name__ == "__main__":
    random_connected_graph = generate_connected_graph(12)
    print("Adjacency matrix\n")
    print_array(random_connected_graph)
    #
    distance_matrix, previous_matrix = dijkstra_algorithm(random_connected_graph)
    print()
    print_dijkstra_algorithm_result(distance_matrix, previous_matrix)
    vertices_distance_matrix = generate_vertices_distance_matrix(random_connected_graph)
    print("\nGraph distance matrix\n")
    print_array(vertices_distance_matrix)
    graph_center = find_graph_centers(random_connected_graph)
    print(f"\nGraph centers {np.array2string(graph_center, precision=2, separator=', ')[1:-1]}\n")
    graph_minimax_center = find_graph_minimax_centers(random_connected_graph)
    print(f"Mnimax graph centers: {np.array2string(graph_minimax_center, precision=2, separator=', ')[1:-1]}\n")
    print("Minimal spanning tree")
    tree = kruskal_mst(random_connected_graph)
    print_tree(tree)
    # visualize_graph(random_connected_graph, weighted_graph=True)
