import copy

import numpy as np

ex_sample_graph = [
    [0, 10, 3, 6, 0, 0, 0, 0, 0, 0, 0], #s
    [0, 0, 8, 0, 8, 6, 0, 0, 0, 0, 0], #a
    [0, 0, 0, 0, 0, 2, 10, 0, 0, 0, 0], #b
    [0, 0, 0, 0, 9, 0, 1, 0, 0, 0, 0], #c
    [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0], #d
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 7, 0], #e
    [0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0], #f
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7], #g
    [0, 0, 0, 0, 0, 0, 8, 1, 0, 0, 5], #h
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7], #i
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #t
]


def print_net_flow(graph: list):
    for row in graph:
        print(row)


def sum_matrix(m1: list, m2: list):
    res_mat = m1
    for i in range(0, len(m2)):
        for j in range(0, len(m2)):
            res_mat[i][j] += m2[i][j]
    return res_mat


def bfs(graph: np.ndarray, row: int, s: int, t: int, parent: list) -> bool:
    """
      BFS algorithm for finding shortest path between two nodes.

           Parameters:
               graph (np.ndarray): matrix representation of generated flow network
               row (int): matrix row size
               s (int): flow network's source
               t (int): flow network's sink
               parent (list): parent list

           Returns:
               Boolean
       """
    visited = [False] * row
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(graph[u]):
            if visited[ind] is False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def ford_fulkerson(graph: np.ndarray, source: int, sink: int) -> np.ndarray:
    """
        Ford-Fulkerson's algorithm.
        Prints Max Flow into terminal.

           Parameters:
               graph (np.ndarray): matrix representation of generated flow network
               source (int): flow network's source
               sink (int): flow network's sink

           Returns:
               graph (np.ndarray): modified matrix representation of flow network
    """
    row = len(graph)
    parent = [-1] * row
    max_flow = 0

    while bfs(graph, row, source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    print("Max flow: %d" % max_flow)
    return graph


def ford_fulkerson_algorithm(graph: np.ndarray, source: int, sink: int) -> np.ndarray:
    """
    Parameters:
               graph (np.ndarray): matrix representation of generated flow network
               source (int): flow network's source
               sink (int): flow network's sink

           Returns:
               graph (np.ndarray): modified matrix representation of flow network
    """
    tmp = copy.deepcopy(graph)
    ford_fulkerson(tmp, source, sink)
    res_graph = tmp + graph
    return res_graph


def test_ford_fulkerson_algo() -> np.ndarray:
    """
      Test Ford-Fulkerson's algorithm.
      Executes the algorithm using sample data.
    """
    source = 0
    sink = 10
    net_tmp = copy.deepcopy(ex_sample_graph)
    net = ford_fulkerson(np.array(ex_sample_graph), source, sink)
    print("Result: ")
    res_graph = net_tmp + net
    print_net_flow(res_graph)
    return res_graph
