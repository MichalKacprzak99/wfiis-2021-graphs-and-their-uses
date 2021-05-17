from random import randint
from grafy.project2.graph_randomization import create_graph_from_degree_sequence
from grafy.project1.graph_visualization import visualize_graph
from grafy.project1.graph_conversion import adj_list_to_matrix
from typing import List, Dict, Tuple
import copy


def get_edge_amount(graph: Dict[int, list]) -> int:
    """
    Get amount of edges in graph

    Parameters
    ----------
    graph : dict
        A dict that represents the graph

    Returns
    -------
    int
        Amount of edges in graph

    """
    edge_number = 0
    for u in graph:
        for v in graph[u]:
            edge_number += 1
    return edge_number


def even_degree_nodes(graph: Dict[int, list]) -> List[int]:
    """
    Function that returns the amount of even nodes in a graph

    Parameters
    -----------
    graph: Dict[int, list]
        A dict representing a graph (adjacency list)

    Returns
    ----------
    List[int]
        Amount of even nodes in graph
    """

    even_nodes = []
    for u in graph:
        if len(graph[u]) % 2 == 0:
            even_nodes.append(u)
    return even_nodes


def is_eulerian(even_nodes: List[int], graph_len: int):
    """
    Checks if a undirected graph is an Eulerian one

    Parameters
    -----------
    even_nodes: List[int]
        A list of even nodes in a graph
    graph_len: int
        The length of the whole graph

    Returns
    ---------
    boolean
        Whether the graph is Eulerian or not
    """

    return graph_len - len(even_nodes) == 0


def is_bridge(graph: Dict[int, list]) -> bool:
    """
    Check if graph has a bridge, which is an edge that links two parts of the graph

    Parameters
    ----------
    graph : dict
        A dict that represents the graph

    Returns
    -------
    bool
        A bool that tells us whether the edge is a bridge

    """
    start = list(graph)[0]
    visited = {}

    for v in graph:
        visited[v] = -1
    visited[start] = 0
    S = [start]
    while len(S) != 0:
        u = S.pop()
        for v in graph[u]:
            if v in visited and visited[v] == -1:
                visited[v] = 0
                S.append(v)
            visited[u] = 1
    return list(visited.values()).count(1) != len(graph)


def get_euler_graph(n: int, visualize: bool = False) -> List:
    """
    A function generating a Euler graph based on the number of edges specified

    Parameters
    ----------
    n : int
        Amount of edges specified
    visualize: bool
        Variable that specifies if the program should visualize a graph or not

    Returns
    -------
    List
        A list representing the Euler graph in form of an adjacency list

    Raises
    -------
    ValueError
        If n is equal or smaller than 2

    """
    if n <= 2:
        raise ValueError("N has to be greater than 2")

    graph_adj_list = [4, 5, 5]
    even_nodes = []
    while is_eulerian(even_nodes, len(graph_adj_list)) is not True:
        degree_sequence = [randint(1, int(n / 2)) * 2 for x in range(n)]
        graph_adj_list = create_graph_from_degree_sequence(degree_sequence)
        even_nodes = even_degree_nodes(graph_adj_list)

    if visualize:
        visualize_graph(adj_list_to_matrix(graph_adj_list))

    graph_copy = copy.copy(graph_adj_list)
    euler_cycle = []
    u = list(graph_copy.keys())[0]

    while get_edge_amount(graph_copy) > 0:
        current_vertex = u
        for u in list(graph_copy[current_vertex]):
            graph_copy[current_vertex].remove(u)
            graph_copy[u].remove(current_vertex)

            bridge = is_bridge(graph_copy)
            if bridge:
                graph_copy[current_vertex].append(u)
                graph_copy[u].append(current_vertex)
            else:
                break
        if bridge:
            if u in graph_copy[current_vertex]:
                graph_copy[current_vertex].remove(u)
            if current_vertex in graph_copy[u]:
                graph_copy[u].remove(current_vertex)
            graph_copy.pop(current_vertex)
        euler_cycle.append((current_vertex, u))

    return euler_cycle


def print_euler_cycle(array: List[Tuple[int, int]]):
    """
    Print the euler cycle. Function adds 1 to vertex numbers, so to represent real-life indexing, in Python we index
    from 0, so the data provided has to represent that accordingly.

    Parameters
    ----------
    array : List
        A list that represents the euler graph as an adjacency list

    Raises
    ----------
    IndexError
        If length of list is 0

    """
    try:
        result = ''.join('%s->' % str(x[0] + 1) for x in array)
        result += str(array[-1][1] + 1)
        print(result)
    except IndexError:
        raise IndexError("List needs to have more than 0 elements")


if __name__ == "__main__":
    print_euler_cycle(get_euler_graph(4, True))
