import numpy as np

from typing import Tuple, List

from grafy.project3.dijkstra_algorithm import dijkstra_algorithm
from grafy.project4.bellman_ford import bellman_ford


def add_s(G: np.ndarray, w: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Function adding additional node s to graph

    Parameters
    ----------
    G: np.ndarray
        A numpy array representing a adjacency matrix
    w: np.ndarray
        A numpy array representing a weighted adjacency matrix

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        Tuple containing modified G and w arrays with additional node

    """
    vertices_number, _ = G.shape
    w_prim = np.zeros((vertices_number + 1, vertices_number + 1))
    g_prim = np.zeros((vertices_number + 1, vertices_number + 1))
    for i in range(vertices_number):
        w_prim[i] = np.insert(w[i], vertices_number, 0)
        g_prim[i] = np.insert(G[i], vertices_number, 0)
    s_distance_row = [0] * (vertices_number + 1)
    s_distance_row[vertices_number] = 0
    w_prim[vertices_number] = np.asarray(s_distance_row)

    neighbour_nodes = [1] * (vertices_number + 1)
    neighbour_nodes[vertices_number] = 0
    g_prim[vertices_number] = np.asarray(neighbour_nodes)

    return g_prim, w_prim


def johnson(G: np.ndarray, w: np.ndarray) -> List[np.ndarray]:
    """Function generating distance matrix for weighted graph

    Parameters
    ----------
    G: np.ndarray
        A numpy array representing a adjacency matrix
    w: np.ndarray
        A numpy array representing a weighted adjacency matrix

    Returns
    -------
    List[List]
        2D array representing the distance matrix

    Raises
    --------
    ValueError
        When a negative cycle has been found in the array

    """

    vertices_number, _ = G.shape
    g_prim, w_prim = add_s(G, w)

    w_dashed = np.zeros((vertices_number + 1, vertices_number + 1))

    h = bellman_ford(g_prim, w_prim, vertices_number)

    if h[0] is False:
        raise ValueError('A negative cycle has been found in the graph. The algorithm cannot proceed')

    for u in range(vertices_number + 1):
        for v in range(vertices_number + 1):
            if g_prim[u][v] == 1:
                w_dashed[u][v] = w_prim[u][v] + h[1][u] - h[1][v]

    D = [np.zeros(vertices_number) for _ in range(vertices_number)]

    for u in range(vertices_number):

        distance = dijkstra_algorithm.dijkstra_algorithm(w_dashed, u + 1)[0]
        for v in range(vertices_number):
            D[u][v] = distance[v] - h[1][u] + h[1][v]

    return D
