import numpy as np
from grafy.project3.dijkstra_algorithm import init, relax
from grafy.project1 import graph_conversion
from typing import Tuple, Union, List, Dict
import copy
import random


def assign_weights_to_adj_matrix(adj_matrix: np.ndarray) -> np.ndarray:
    """Function assigns weights to a given adjacency matrix

    Parameters
    ----------
    adj_matrix: np.ndarray
        Adjacency matrix we assign weights to

    Returns
    -------
    np.ndarray
        A numpy array representing the adjacency matrix with added weights

    """
    adj_matrix_weighted = copy.deepcopy(adj_matrix)
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                adj_matrix_weighted[i][j] = random.randint(-5, 11)

    return adj_matrix_weighted
# G - graph matrix, w - weighted matrix, s - start vertex


def bellman_ford(G: np.ndarray, w: np.ndarray, s: int) -> Tuple[bool, np.ndarray, np.ndarray]:
    """Function assigns weights to a given adjacency matrix

    Parameters
    ----------
    G: np.ndarray
        A numpy array representing the graph we want to analyze
    w: np.ndarray
        A weighted numpy array we access weight values from
    s: int
        The number of the starting node

    Returns
    -------
    Tuple[bool, np.ndarray, np.ndarray]
        Tuple with info about whether a negative cycle has been found in the graph, an array of shortest paths from s
        to other nodes and an array of previous nodes in shortest paths
    bool
        True if a negative cycle has been found in the graph
    np.ndarray
        d_s(v) array of shortest paths from s to v
    np.ndarray
        p_s(v) array of previous node in shortest path

    Raises
    -------
    ValueError
        when G and w are of different dimensions

    """
    if G.shape != w.shape:
        raise ValueError("The graph matrix and weighted matrix are of different shapes")

    vertices_number, _ = G.shape
    d_s, p_s = init(vertices_number, s)
    adj_list = graph_conversion.adj_matrix_to_list(G)

    for i in range(vertices_number - 1):
        for u in range(vertices_number):
            for v in adj_list[u]:
                relax(u, v, w[u][v], d_s, p_s)

    for u in range(vertices_number):
        for v in adj_list[u]:
            if d_s[v] > d_s[u] + w[u][v]:
                return False, d_s, p_s
    return True, d_s, p_s
