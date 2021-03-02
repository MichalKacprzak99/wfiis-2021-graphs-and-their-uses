import numpy as np
from random import randint


def generate_N_L_graph(vertices_number: int, edges_number: int):
    generate_edges = set()
    edge = (randint(0, vertices_number-1), randint(0, vertices_number-1))
    while len(generate_edges) < edges_number:
        while edge in generate_edges or set(reversed(edge)) in generate_edges or edge[0] >= edge[1]:
            edge = (randint(0, vertices_number-1), randint(0, vertices_number-1))
        generate_edges.add(edge)
    graph = np.zeros((vertices_number, vertices_number))

    for edge in generate_edges:
        start_vertex, end_vertex = edge
        graph[start_vertex, end_vertex] = 1

    return graph + np.transpose(graph)


def generate_N_P_graph(vertices_number: int, edges_probability: float):
    graph = np.random.choice([0, 1], (vertices_number, vertices_number), p=[1-edges_probability, edges_probability])
    graph = np.tril(graph, -1)
    return graph + np.transpose(graph)
