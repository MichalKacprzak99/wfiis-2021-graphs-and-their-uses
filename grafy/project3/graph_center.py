import numpy
import numpy as np
from grafy.project3.dijkstra_algorithm import dijkstra_algorithm


def generate_vertices_distance_matrix(graph_matrix: np.ndarray) -> np.ndarray:
    """Generate matrix which contains distance between each pair of vertices in graph

    Function run Dijkstra algorithm for each vertex in graph

    Parameters
    ----------
    graph_matrix : np.ndarray
        adjacency matrix of graph
    Returns
    -------
        np.ndarray
    """
    distance_matrix = np.zeros(shape=graph_matrix.shape)
    vertices_number, _ = graph_matrix.shape
    for vertex in range(vertices_number):
        d_s, _ = dijkstra_algorithm(graph_matrix, vertex+1)
        distance_matrix[vertex, :] = d_s

    return distance_matrix


def find_graph_centers(graph_matrix: np.array) -> numpy.array:
    """Function calculate centers of graph

    Function, based on graph_matrix, create distance matrix of graph.
    Then calculate centers of graph.

    Parameters
    ----------
    graph_matrix :
        adjacency matrix of graph
    Returns
    -------
    list
        centers of graph
    """
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    vertex_distances_sum = np.sum(distance_matrix, axis=0)
    graph_centers = np.flatnonzero(vertex_distances_sum == vertex_distances_sum.min()) + 1
    return graph_centers


def find_graph_minimax_centers(graph_matrix: np.array) -> numpy.array:
    """Function calculate minimax centers of graph

    Function, based on graph_matrix, create distance matrix of graph.
    Then calculate minimax centers of graph

    Parameters
    ----------
    graph_matrix :
        adjacency matrix of graph
    Returns
    -------
    list
        minimax centers of graph
    """
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    vertex_max_distance = np.max(distance_matrix, axis=0)
    graph_minimax_centers = np.flatnonzero(vertex_max_distance == vertex_max_distance.min()) + 1
    return graph_minimax_centers
