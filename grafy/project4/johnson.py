import copy
from typing import Tuple

import numpy as np
import random
from grafy.project4 import bellman_ford
from grafy.project1 import graph_conversion
from grafy.project3 import dijkstra_algorithm


def add_s(G: np.ndarray, w: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
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


def johnson(G: np.ndarray, w: np.ndarray):

    vertices_number, _ = G.shape
    g_prim, w_prim = add_s(G, w)

    distance = []

    w_dashed = np.zeros((vertices_number + 1, vertices_number + 1))

    h = bellman_ford.bellman_ford(g_prim, w_prim, vertices_number)

    if h[0] is False:
        print('A negative cycle has been found in the graph. The algorithm cannot proceed')
        return

    for u in range(vertices_number + 1):
        for v in range(vertices_number + 1):
            if g_prim[u][v] == 1:
                w_dashed[u][v] = w_prim[u][v] + h[1][u] - h[1][v]

    D = [[] for i in range(vertices_number)]

    for u in range(vertices_number):
        D[u].extend(0 for _ in range(vertices_number))

        distance = dijkstra_algorithm.dijkstra_algorithm(w_dashed, u + 1)[0]
        for v in range(vertices_number):
            D[u][v] = distance[v] - h[1][u] + h[1][v]

    return D

