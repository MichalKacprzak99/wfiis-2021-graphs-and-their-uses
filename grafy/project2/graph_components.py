from typing import List, DefaultDict, Dict

from grafy.project1.graph_conversion import adj_matrix_to_list
from collections import defaultdict


def recursive_components(comp_number: int, vertex: int, graph: Dict[int, list], comps: List[int]):
    """
    Recursive helper function for finding components

    Parameters
    ----------
    comp_number : int
        A numpy array that represents the adjacency matrix

    vertex: int
        Value that specifies from which vertex we traverse the graph

    graph: dict
        A dict representing the graph we traverse

    comps: List[int]
        A list of all components of the graph
    """
    for u in graph[vertex]:
        if comps[u] == -1:
            comps[u] = comp_number
            recursive_components(comp_number, u, graph, comps)


def find_biggest_graph_component(graph: Dict[int, list]):
    """
    Function that finds and prints all components and the biggest one

    Parameters
    ----------
    graph : dict
        A dict that represents the graph as an adjacency list

    """
    comp_number = 0
    comps = [-1] * len(graph.keys())

    for v in graph.keys():
        if comps[v] == -1:
            comp_number += 1
            comps[v] = comp_number
            recursive_components(comp_number, v, graph, comps)

    comps_representation = defaultdict(list)

    for i, e in enumerate(comps):
        comps_representation[e].append(i + 1)

    biggest_comp = 0
    biggest_comp_length = 0

    for comp, comp_vertices in sorted(comps_representation.items()):
        if len(comp_vertices) > biggest_comp_length:
            biggest_comp = comp
            biggest_comp_length = len(comp_vertices)
        print(f'{comp}: {comp_vertices}')

    print(f"Najwieksza skladowa ma numer {biggest_comp}")


if __name__ == "__main__":

    graph_N_L = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 ]

    adj_list = adj_matrix_to_list(graph_N_L)

    find_biggest_graph_component(adj_list)
