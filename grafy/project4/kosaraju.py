from collections import defaultdict

import numpy as np

from grafy.project1.graph_conversion import adj_matrix_to_list


def kosaraju(G: np.ndarray) -> dict:
    """Function implementing Kosaraju's algorithm, which returns connected components

    Parameters
    ----------
    G: np.ndarray
        A numpy array representing a adjacency matrix

    Returns
    -------
    dict
        A dictionary that represents connected components in graph, if it has only one key digraph is strongly connected

    """
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

    to_return = defaultdict(list)
    for item, index in enumerate(comp):
        if item != 0:
            to_return[index].append(item)

    return to_return


def DFS_visit(v: int, G: dict, d: np.ndarray, f: np.ndarray, t: int) -> int:
    t += 1
    d[v] = t
    if v in G:
        for u in G[v]:
            if d[u] == -1:
                t = DFS_visit(u, G, d, f, t)
    t = t + 1
    f[v] = t
    return t


def components_r(nr: int, v: int, Gt: dict, comp: np.ndarray):
    if v in Gt:
        for u in Gt[v]:
            if comp[u] == -1:
                comp[u] = nr
                components_r(nr, u, Gt, comp)
