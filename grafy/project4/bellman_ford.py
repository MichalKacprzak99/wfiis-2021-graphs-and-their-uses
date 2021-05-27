import numpy as np
from grafy.project3.dijkstra_algorithm import init, relax
from grafy.project1 import graph_conversion
from typing import Tuple, Union, List, Dict
import copy
import random


def matrix_assign_weights(adj_matrix: np.ndarray) -> np.ndarray:
    adj_matrix_weighted = copy.deepcopy(adj_matrix)
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                adj_matrix_weighted[i][j] = random.randint(-5, 11)

    return adj_matrix_weighted


def wmatrix_to_wlist(adj_matrix_weighted: np.ndarray) -> List[List[Union[int, Dict[str, float]]]]:
    weighted_list = []
    for i in range(len(adj_matrix_weighted)):
        for j in range(len(adj_matrix_weighted[0])):
            if adj_matrix_weighted[i][j] != 0:
                weighted_list.append([i+1, j+1, {'weight': adj_matrix_weighted[i][j]}])
    return weighted_list

# G - graph matrix, w - weighted matrix, s - start vertex


def bellman_ford(G: np.ndarray, w: np.ndarray, s: int) -> Tuple[bool, np.ndarray, np.ndarray]:

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
