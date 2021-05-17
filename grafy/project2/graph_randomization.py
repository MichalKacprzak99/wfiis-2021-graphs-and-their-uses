from collections import defaultdict, OrderedDict
import random
from typing import DefaultDict, List, Dict

from grafy.project1.graph_conversion import adj_list_to_matrix
from grafy.project1.graph_visualization import visualize_graph


def create_graph_from_degree_sequence(degree_sequence: List[int]) -> Dict[int, list]:
    """
    Create graph from degree sequence

    Parameters
    ----------
    degree_sequence : list
        A list that represents the degree sequence

    Returns
    -------
    dict
        A dict that represents the graph constructed

    """
    adjacency_list = defaultdict(list)
    degree_sequence = list(sorted(degree_sequence, reverse=True))
    degree_sequence = OrderedDict(zip(range(len(degree_sequence)), degree_sequence))

    while True:
        vertex, degree = degree_sequence.popitem(last=False)
        for index, (key, value) in enumerate(degree_sequence.items()):
            if index < degree:
                degree_sequence[key] -= 1
                adjacency_list[key].append(vertex)
                adjacency_list[vertex].append(key)

        sorted_sequence = sorted(degree_sequence.items(), key=lambda kv: kv[1], reverse=True)
        degree_sequence = OrderedDict(sorted_sequence)
        if sum(degree_sequence.values()) == 0:
            break
    return adjacency_list


def swap_edges(x1: int, x2: int, y1: int, y2: int, adjacency_list: Dict[int, list]):
    """
    Swap edges in adjacency list

    Parameters
    ----------
    x1 : int
        Start of the first edge

    x2 : int
        End of the first edge

    y1 : int
        Start of the second edge

    y2 : int
        End of the second edge

    adjacency_list: dict
        A dict that represents the adjacency list

    """
    adjacency_list[x1].append(y1)
    adjacency_list[y1].append(x1)
    adjacency_list[x2].append(y2)
    adjacency_list[y2].append(x2)


def delete_edge(x1: int, x2: int, adjacency_list: Dict[int, list]):
    """
    Delete edge from graph

    Parameters
    ----------
    x1 : int
        Start of the edge

    x2 : int
        End of the edge

    adjacency_list: dict
        A dict representing the adjacency_list

    """
    adjacency_list[x1].remove(x2)
    adjacency_list[x2].remove(x1)


def randomize_graph(degree_sequence: List[int], swap_number: int) -> Dict[int, list]:
    """
    Randomize a graph

    Parameters
    ----------
    degree_sequence: list
        A degree sequence represented by a list from which we construct a graph

    swap_number: int
        Number of swaps to be performed on the graph

    Returns
    -------
    dict
        A dict representing the result adjacency list

    """
    adjacency_list = create_graph_from_degree_sequence(degree_sequence)

    for _ in range(swap_number):
        while True:
            x1, y1 = random.sample(list(adjacency_list.keys()), k=2)

            if y1 not in adjacency_list[x1] and len(adjacency_list[x1]) > 0 and len(adjacency_list[y1]) > 0:

                x2 = random.sample([vertex for vertex in adjacency_list[x1] if vertex != x1], k=1)[0]
                y2 = random.sample([vertex for vertex in adjacency_list[y1] if vertex != y1], k=1)[0]

                if x2 == y2 or y2 in adjacency_list[x2] and (x2 in adjacency_list[y1] or y2 in adjacency_list[x1]):
                    pass
                else:
                    delete_edge(x1, x2, adjacency_list)
                    delete_edge(y1, y2, adjacency_list)
                    if x2 not in adjacency_list[y2]:
                        swap_edges(x1, x2, y1, y2, adjacency_list)
                    else:
                        swap_edges(x1, x2, y2, y1, adjacency_list)
                    break

    return adjacency_list


def generate_regular_graph(vertices_number: int, k_degree: int):
    """
    Generate a regular graph based on the number of vertices and k degree and visualize it

    Parameters
    ----------
    vertices_number: int
        Amount of vertices in graph

    k_degree : int
        Amount of edges connected to every vertex


    """
    if vertices_number >= k_degree + 1 and vertices_number * k_degree % 2 == 0:
        degree_sequence = [k_degree] * vertices_number

        adj_matrix = adj_list_to_matrix(randomize_graph(degree_sequence, 100))
        visualize_graph(adj_matrix)


if __name__ == "__main__":
    generate_regular_graph(7, 2)
