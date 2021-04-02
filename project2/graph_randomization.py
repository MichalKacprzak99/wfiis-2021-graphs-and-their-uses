from collections import defaultdict, OrderedDict
import random
from typing import DefaultDict, List

from project1.graph_conversion import adj_list_to_matrix
from project1.graph_visualization import visualize_graph


def create_graph_from_degree_sequence(degree_sequence: List[int]) -> DefaultDict[int, list]:
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


def swap_edges(x1: int, x2: int, y1: int, y2: int, adjacency_list: DefaultDict[int, list]):
    adjacency_list[x1].append(y1)
    adjacency_list[y1].append(x1)
    adjacency_list[x2].append(y2)
    adjacency_list[y2].append(x2)


def delete_edge(x1: int, x2: int, adjacency_list: DefaultDict[int, list]):
    adjacency_list[x1].remove(x2)
    adjacency_list[x2].remove(x1)


def randomize_graph(degree_sequence: List[int], swap_number: int) -> DefaultDict[int, list]:
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
    if vertices_number >= k_degree + 1 and vertices_number * k_degree % 2 == 0:
        degree_sequence = [k_degree] * vertices_number

        adj_matrix = adj_list_to_matrix(randomize_graph(degree_sequence, 100))
        visualize_graph(adj_matrix)


if __name__ == "__main__":
    generate_regular_graph(7, 2)
