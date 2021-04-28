import numpy as np
from graph_conversion import adj_matrix_to_list, print_adj_list
from typing import DefaultDict


def kosaraju(G: np.ndarray):
    d = np.full(G.shape[0], -1)
    f = np.full(G.shape[0], -1)
    t = 0
    adj_list = adj_matrix_to_list(G)
    for vertex in adj_list:
        if d[vertex] == -1:
            DFS_visit(vertex, adj_list, d, f, t)
    Gt = np.transpose(G)
    adj_list = adj_matrix_to_list(Gt)
    nr = 0
    comp = np.full(G.shape[0], -1)

    for v in np.sort(f)[::-1]:
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_r(nr, v, adj_list, comp)
    print(comp)


# v - wierzchołek;
# G - graf;
# d - tablica czasów odwiedzenia;
# f - tablica czasów przetworzenia;
# t - czas przetworzenia;


def DFS_visit(v: int, G: DefaultDict[int, list], d: np.ndarray, f: np.ndarray, t: int):
    t += 1
    d[v] = t
    if v in G:
        for u in G[v]:
            if d[u] != -1:
                break
            DFS_visit(u, G, d, f, t)
    t = t + 1
    f[v] = t


def components_r(nr: int, v: int, Gt: DefaultDict[int, list], comp: np.ndarray):
    if v in Gt:
        for u in Gt[v]:
            if comp[u] != -1:
                break
            comp[u] = nr
            components_r(nr, u, Gt, comp)
