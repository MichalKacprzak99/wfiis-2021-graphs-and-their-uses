import numpy as np
from graph_conversion import adj_matrix_to_list
from typing import DefaultDict


def kosaraju(G: np.ndarray) -> np.ndarray:
    d = np.full(G.shape[0], -1)
    f = np.full(G.shape[0], -1)
    t = 0
    adj_list = adj_matrix_to_list(G)
    for vertex in adj_list:
        if d[vertex] == -1:
            t = DFS_visit(vertex, adj_list, d, f, t)
    Gt = np.transpose(G)
    adj_list = adj_matrix_to_list(Gt)
    nr = 0
    comp = np.full(G.shape[0], -1)

    for i in range(G.shape[0]):
        adj_list[i]

    sorted_by_times_reverse = sorted(adj_list.keys(), key=lambda x: f[x], reverse=True)

    for v in sorted_by_times_reverse:
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_r(nr, v, adj_list, comp)
    return comp


def DFS_visit(v: int, G: DefaultDict[int, list], d: np.ndarray, f: np.ndarray, t: int) -> int:
    t += 1
    d[v] = t
    if v in G:
        for u in G[v]:
            if d[u] == -1:
                t = DFS_visit(u, G, d, f, t)
    t = t + 1
    f[v] = t
    return t


def components_r(nr: int, v: int, Gt: DefaultDict[int, list], comp: np.ndarray):
    if v in Gt:
        for u in Gt[v]:
            if comp[u] == -1:
                comp[u] = nr
                components_r(nr, u, Gt, comp)
