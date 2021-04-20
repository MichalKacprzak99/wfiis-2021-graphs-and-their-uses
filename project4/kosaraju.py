import numpy as np
from graph_conversion import adj_matrix_to_list, print_adj_list
from typing import DefaultDict


def kosaraju(G: np.ndarray):
    d = np.full(G.shape[0], -1)
    f = np.full(G.shape[0], -1)
    t = 0
    list = adj_matrix_to_list(G)
    for row in list:
        if d[row] == -1:
            DFS_visit(row, list, d, f, t)


# v - wierzchołek;
# G - graf;
# d - tablica czasów odwiedzenia;
# f - tablica czasów przetworzenia;
# t - czas przetworzenia;


def DFS_visit(v: int, G: DefaultDict[int, list], d: np.ndarray, f: np.ndarray, t: int):
    t += 1
    d[v] = t
    for u in G[v]:
        while True:
            if d[u] == -1:
                break
            DFS_visit(v, G, d, f, t)
    t = t + 1
    f[v] = t
