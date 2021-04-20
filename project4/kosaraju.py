import numpy as np
from graph_conversion import adj_matrix_to_list, print_adj_list


# def kosaraju(graph: np.ndarray):


# v - wierzchołek;
# G - graf;
# d - tablica czasów odwiedzenia;
# f - tablica czasów przetworzenia;
# t - czas przetworzenia;


def DFS_visit(v: int, G: np.ndarray, d: np.ndarray, f: np.ndarray, t: int):
    t += 1
    d[v] = t

