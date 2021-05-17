import numpy as np
from grafy.project3.dijkstra_algorithm import init, relax
from grafy.project1 import graph_conversion


def bellman_ford(graph_matrix: np.ndarray, start_vertex: int) -> bool:
    vertices_number, _ = graph_matrix.shape
    d_s, p_s = init(vertices_number, start_vertex)
    adj_list = graph_conversion.adj_matrix_to_list(graph_matrix)

    for i in range(1, vertices_number - 1):
        for u in range(vertices_number):
            for v in adj_list[u]:
                relax(u, v, graph_matrix[u][v], d_s, p_s)

    for u in range(vertices_number):
        for v in adj_list[u]:
            if d_s[v] > d_s[u] + graph_matrix[u][v]:
                return False
    return True
