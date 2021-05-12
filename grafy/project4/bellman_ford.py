from project3.dijkstra_algorithm import init, relax
import numpy as np


# Bellman_Ford(G, w, s) // n – liczba wierzchołków
# 1. Init(G, s)
# 2. for i = 1 to n − 1
# 3. do for każda krawędź (u, v) należąca do grafu G
# 4. do Relax(u, v, w)
# 5. for każda krawędź (u, v) należąca do grafu G
# 6. do if ds(v) > ds(u) + w(u, v)
# 7. then return False // W grafie jest cykl o ujemnej wadze osiągalny ze źródła s
# 8. return True


def bellman_ford(graph_matrix: np.ndarray, start_vertex: int):
    vertices_number, _ = graph_matrix.shape
    d_s, p_s = init(vertices_number, start_vertex)
    for i in range(1, vertices_number - 1):
        for u, v in enumerate(graph_matrix[:]):

