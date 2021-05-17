import numpy as np
from typing import List, Tuple


def init(vertices_number: int, start_vertex: int) -> Tuple[np.ndarray, np.ndarray]:
    """Set initial values of "distance" and "previous" array

    All values of "distance" array are set to Infinity,
    except start vertex because distance from start vertex to start vertex is zero
    Previous vertex on path are unknown so values in "previous" array are set to are set to nan

    Parameters
    ----------
    vertices_number : int
        number of vertices in graph
    start_vertex : int
        it is initial vertex for algorithm, paths will be calculate from this vertex to the rest
    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        ("distance" array, "previous" array)
    """

    d_s = np.full(vertices_number, np.Inf)
    p_s = np.full(vertices_number, np.nan)
    d_s[start_vertex] = 0
    return d_s, p_s


def relax(u: int, v: int, w: int, d_s: np.ndarray, p_s: np.array):
    if d_s[v] > d_s[u] + w:
        d_s[v] = d_s[u] + w
        p_s[v] = u


def find_vertex_with_min_d_s(S: np.ndarray, d_s: np.ndarray) -> int:
    """Function for finding not accepted vertex with smallest distance

    Parameters
    ----------
    S : numpy.array
        array which contains "accepted" vertex
    d_s : numpy.array
        array with distances from start vertex
    Returns
    -------
    int
        number of vertex with smallest distance
    """

    vertex_with_min_distance = 0
    min_weight = np.Inf
    for index, weight in enumerate(d_s):
        if index in S:
            continue
        if weight < min_weight:
            vertex_with_min_distance = index
            min_weight = weight
    return vertex_with_min_distance


def dijkstra_algorithm(graph_matrix: np.ndarray, start_vertex: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """ Implementation of Dijkstra algorithm

    Parameters
    ----------
    graph_matrix : numpy.ndarray
        adjacency matrix of graph with non-negative weight

    start_vertex : int
        it is initial vertex for algorithm, paths will be calculate from this vertex to the rest
    Returns
    -------
    tuple(np.ndarray, np.ndarray)
        tuple which contains distance array and array with previous vertex on the path

    Raises
    ------
    ValueError:
        If any cell in graph_matrix is negative
        If start vertex is negative or greater than vertices number in graph

    """

    if np.any(graph_matrix < 0):
        raise ValueError("Dijkstra's algorithm does not support negative edge weights")

    vertices_number, _ = graph_matrix.shape
    start_vertex -= 1
    if start_vertex >= vertices_number or start_vertex < 0:
        raise ValueError(f"Value of start vertex must be between 1 and {vertices_number}")

    d_s, p_s = init(vertices_number, start_vertex)
    S = np.empty(0, dtype=np.int64)
    while len(S) != vertices_number:
        u = find_vertex_with_min_d_s(S, d_s)
        S = np.sort(np.concatenate((S, np.array([u]))))
        for v, w in enumerate(graph_matrix[:, u]):
            if v in S or w == 0:
                continue
            relax(u, v, w, d_s, p_s)
    return d_s, p_s


def generate_shortest_paths(p_s: np.ndarray) -> List[List[int]]:
    """Function generates path based on previous vertices stored in p_s

    Parameters
    ----------
    p_s : np.ndarray
        array which contains previous vertex on path
    Returns
    -------
    List[List[int]]
    """
    paths = [[] for _ in p_s]
    finished_vertices = []

    while len(p_s) != len(finished_vertices):
        for vertex, previous_vertex in enumerate(p_s):
            if vertex in finished_vertices:
                continue
            elif np.isnan(previous_vertex):
                paths[vertex].append(vertex + 1)
                finished_vertices.append(vertex)
            elif len(paths[int(previous_vertex)]) != 0:
                paths[vertex].extend([*paths[int(previous_vertex)], vertex + 1])
                finished_vertices.append(vertex)
    return paths


def print_dijkstra_algorithm_result(d_s: np.ndarray, p_s: np.ndarray):
    """Function for nice results printing of Dijkstra algorithm

    Parameters
    ----------
    d_s : np.ndarray
        array with distances from start vertex
    p_s : np.ndarray
        array which contains previous vertex on path
    """
    start_vertex = np.isnan(p_s).argmax()
    paths = generate_shortest_paths(p_s)
    print("Shortest paths from start vertex to others\n")
    print(f"Start vertex: {start_vertex + 1}\n")
    for vertex, (length, path) in enumerate(zip(d_s, paths)):
        print(f'vertex: {vertex + 1:2.0f}; path length:{length:2.0f}; path: {path}')
