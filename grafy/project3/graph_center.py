import numpy as np
from .dijkstra_algorithm import dijkstra_algorithm


def generate_vertices_distance_matrix(graph_matrix: np.ndarray) -> np.ndarray:
    distance_matrix = np.zeros(shape=graph_matrix.shape)
    vertices_number, _ = graph_matrix.shape
    for vertex in range(vertices_number):
        d_s, _ = dijkstra_algorithm(graph_matrix, vertex+1)
        distance_matrix[vertex, :] = d_s

    return distance_matrix


def find_graph_center(graph_matrix: np.ndarray) -> int:
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    graph_center = np.argmin(np.sum(distance_matrix, axis=0)) + 1
    return graph_center


def find_graph_minimax_center(graph_matrix: np.ndarray) -> int:
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    graph_minimax_center = np.argmin(np.max(distance_matrix, axis=0)) + 1
    return graph_minimax_center
