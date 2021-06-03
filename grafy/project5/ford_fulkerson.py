import copy
import numpy as np


class WrongInputException(Exception):
    pass


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


def bfs(graph: np.ndarray, row: int, s: int, t: int, parent: list) -> bool:
    """
      BFS algorithm for finding shortest path between two nodes.
      Fills parent list to store the path.

           Parameters:
               graph (np.ndarray): matrix representation of generated flow network
               row (int): matrix row size
               s (int): flow network's source
               t (int): flow network's sink
               parent (list): parent list

           Returns:
               true (bool): if there is a path from source to sink in residual graph
               false (bool): if there is not
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


def ford_fulkerson_algorithm(graph: np.ndarray, source: int, sink: int) -> np.ndarray:
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

    residual_graph = copy.deepcopy(graph)
    row = len(residual_graph)
    parent = [-1] * row
    max_flow = 0
    
    if source == sink or sink < 0 or source < 0 or source >= row or sink >= row:
      raise WrongInputException('Wrong input source/sink vertice(s)')

    while bfs(residual_graph, row, source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
    print("Max flow: %d" % max_flow)

    return residual_graph


def test_ford_fulkerson_algo() -> np.ndarray:
    """
      Test Ford-Fulkerson's algorithm.
      Executes the algorithm using sample data.
    """
    res = ford_fulkerson_algorithm(np.array(ex_sample_graph), 0, 10)
    print("Result: ")
    print(res)
    return res

