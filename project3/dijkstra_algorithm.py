import numpy as np
from typing import List, Tuple
import pretty_errors

graph_N_L_1 = [[0, 8, 0, 9, 3, 9, 5],
               [8, 0, 0, 2, 4, 0, 1],
               [0, 0, 0, 0, 0, 4, 0],
               [9, 2, 0, 0, 0, 9, 0],
               [3, 4, 0, 0, 0, 4, 0],
               [9, 0, 4, 9, 4, 0, 0],
               [5, 1, 0, 0, 0, 0, 0]]


def init(vertex_number: int, start_vertex: int) -> Tuple[list, list]:
    d_s = [np.Inf] * vertex_number
    p_s = [None] * vertex_number
    d_s[start_vertex] = 0
    return d_s, p_s


def relax(u: int, v: int, w: int, d_s: list, p_s: list):
    if d_s[v] > d_s[u] + w:
        d_s[v] = d_s[u] + w
        p_s[v] = u


def find_vertex_with_min_d_s(S, d_s) -> int:
    vertex_with_min_ds = 0
    min_weight = np.Inf
    for index, weight in enumerate(d_s):
        if index in S:
            continue
        if weight < min_weight:
            vertex_with_min_ds = index
            min_weight = weight
    return vertex_with_min_ds


def dijkstra_algorithm(graph_matrix: np.ndarray, start_vertex: int = 0) -> Tuple[list, list]:

    if np.any(graph_matrix < 0):
        raise ValueError("Dijkstra's algorithm does not support negative edge weights")

    vertices_number, _ = graph_matrix.shape
    d_s, p_s = init(vertices_number, start_vertex)
    graph_vertices = list(range(vertices_number))
    S = []
    while S != graph_vertices:
        u = find_vertex_with_min_d_s(S, d_s)
        S.append(u)
        S.sort()
        for v, w in enumerate(graph_matrix[:, u]):
            if v in S or w == 0:
                continue
            relax(u, v, w, d_s, p_s)
    return d_s, p_s


def generate_shortest_paths(p_s: list) -> List[List[int]]:
    paths = [[] for _ in p_s]
    finished_vertices = []
    while len(p_s) != len(finished_vertices):
        for vertex, previous_vertex in enumerate(p_s):
            if vertex in finished_vertices:
                continue
            elif previous_vertex is None:
                paths[vertex].append(vertex + 1)
                finished_vertices.append(vertex)
            elif len(paths[previous_vertex]) != 0:
                paths[vertex].extend([*paths[previous_vertex], vertex + 1])
                finished_vertices.append(vertex)
    return paths


def print_dijkstra_algorithm(d_s: list, p_s: list):
    start_vertex = p_s.index(None)
    paths = generate_shortest_paths(p_s)
    print("Shortest paths from start vertex to others\n")
    print(f"Start vertex: {start_vertex + 1}\n")
    for vertex, (length, path) in enumerate(zip(d_s, paths)):
        print(f'vertex: {vertex + 1}; path length: {length}; path: {path}')
