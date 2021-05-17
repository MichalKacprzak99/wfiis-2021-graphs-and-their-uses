import numpy as np
from grafy.project1.graph_generation import generate_N_L_graph


def generate_connected_graph(vertices_number: int) -> np.ndarray:
    """Function generate random connected graph with given number of vertices

    Parameters
    ----------
    vertices_number : int
        number of vertices in generated graph

    Returns
    -------
    numpy.array
        an array which represents adjacency matrix of generated graph

    Raises
    ______
    ValueError
        If vertices_number is less than 0
    """
    maximum_edges_number = vertices_number * (vertices_number - 1) // 2
    minimum_edges_number = (vertices_number - 1) * (vertices_number - 2) // 2 + 1

    try:
        edges_number = np.random.randint(minimum_edges_number, maximum_edges_number + 1)
    except ValueError:
        raise ValueError("The number of vertices must be positive")

    graph = generate_N_L_graph(vertices_number, edges_number)

    def apply_weight(edge):
        if edge == 1:
            return np.random.randint(1, 11)
        else:
            return edge

    apply_weight = np.vectorize(apply_weight)
    connected_graph = apply_weight(np.tril(graph))
    connected_graph += np.transpose(connected_graph)
    return connected_graph
