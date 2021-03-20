from project1 import graph_conversion
from graph_conversion import adj_matrix_to_list
from collections import defaultdict
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


def recursive_components(comp_number, vertex, graph, comps):
    for u in graph[vertex]:
        if comps[u-1] == -1:
            comps[u-1] = comp_number
            recursive_components(comp_number, u, graph, comps)


def find_biggest_graph_component(graph):
    comp_number = 0
    comps = [-1] * len(graph.keys())

    for v in graph.keys():
        if comps[v-1] == -1:
            comp_number += 1
            comps[v-1] = comp_number
            recursive_components(comp_number, v, graph, comps)

    comps_representation = defaultdict(list)
    for i, e in enumerate(comps):
        comps_representation[e].append(i+1)
    biggest_comp = 0
    biggest_comp_length = 0
    for comp, comp_vertices in sorted(comps_representation.items()):
        if len(comp_vertices) > biggest_comp_length:
            biggest_comp = comp
            biggest_comp_length = len(comp_vertices)
        print(f'{comp}: {comp_vertices}')

    print(f"Najwieksza skladowa ma numer {biggest_comp}")


find_biggest_graph_component(adj_list)
