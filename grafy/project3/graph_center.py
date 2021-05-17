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


def find_graph_center(graph_matrix: np.array) -> int:
    """Function calculate center of graph

    Function, based on graph_matrix, create distance matrix of graph.
    Then calculate center of graph.

    Parameters
    ----------
    graph_matrix :
        adjacency matrix of graph
    Returns
    -------
    int
        center of graph
    """
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    graph_center = np.argmin(np.sum(distance_matrix, axis=0)) + 1
    return graph_center


def find_graph_minimax_center(graph_matrix: np.array) -> int:
    """Function calculate minimax center of graph

    Function, based on graph_matrix, create distance matrix of graph.
    Then calculate minimax center of graph

    Parameters
    ----------
    graph_matrix :
        adjacency matrix of graph
    Returns
    -------
    int
        minimax center of graph
    """
    distance_matrix = generate_vertices_distance_matrix(graph_matrix)
    graph_minimax_center = np.argmin(np.max(distance_matrix, axis=0)) + 1
    return graph_minimax_center
