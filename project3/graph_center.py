import numpy as np
from dijkstra_algorithm import dijkstra_algorithm


def generate_vertices_distance_matrix(graph_matrix):
    distance_matrix = np.zeros(shape=graph_matrix.shape)
    vertices_number, _ = graph_matrix.shape
    for vertex in range(vertices_number):
        d_s, _ = dijkstra_algorithm(graph_matrix, vertex)
        distance_matrix[vertex, :] = d_s

    return distance_matrix


def find_graph_center(graph_matrix):
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    return np.argmin(np.sum(distance_matrix, axis=0)) + 1


def find_graph_minimax_center(graph_matrix):
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    return np.argmin(np.max(distance_matrix, axis=0)) + 1