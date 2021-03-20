from collections import defaultdict, OrderedDict
import random
from project1 import graph_conversion
from graph_conversion import adj_list_to_matrix
from graph_visualization import visualize_graph


def create_graph_from_degree_sequence(degree_sequence: list):
    adjacency_list = defaultdict(list)
    degree_sequence = list(sorted(degree_sequence, reverse=True))
    degree_sequence = OrderedDict(zip([i + 1 for i in range(len(degree_sequence))], degree_sequence))

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


def swap_edge(x1, x2, y1, y2, adjacency_list):
    adjacency_list[x1].append(y1)
    adjacency_list[y1].append(x1)
    adjacency_list[x2].append(y2)
    adjacency_list[y2].append(x2)


def delete_edge(x1, x2, y1, y2, adjacency_list):
    adjacency_list[x1].remove(x2)
    adjacency_list[x2].remove(x1)
    adjacency_list[y1].remove(y2)
    adjacency_list[y2].remove(y1)


def randomize_graph(degree_sequence: list, swap_number: int):
    adjacency_list = create_graph_from_degree_sequence(degree_sequence)

    for _ in range(swap_number):
        while True:
            x1, y1 = random.sample(list(adjacency_list.keys()), k=2)

            if y1 not in adjacency_list[x1] and len(adjacency_list[x1]) > 0 and len(adjacency_list[y1]) > 0:

                x2 = random.sample([vertex for vertex in adjacency_list[x1] if vertex != x1], k=1)[0]
                y2 = random.sample([vertex for vertex in adjacency_list[y1] if vertex != y1], k=1)[0]
                if x2 == y2:
                    pass

                if y2 in adjacency_list[x2] and (x2 in adjacency_list[y1] or y2 in adjacency_list[x1]):
                    pass
                else:
                    delete_edge(x1, x2, y1, y2)
                    if x2 not in adjacency_list[y2]:
                        swap_edge(x1, x2, y1, y2, adjacency_list)
                    else:
                        swap_edge(x1, x2, y2, y1, adjacency_list)
                    break

    return adjacency_list


tmp = create_graph_from_degree_sequence([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2])

tmp1 = randomize_graph([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2], 10)

visualize_graph(adj_list_to_matrix(tmp1))
