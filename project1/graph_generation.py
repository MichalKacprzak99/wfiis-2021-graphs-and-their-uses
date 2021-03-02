import numpy as np
import random


def generate_N_L_graph(vertices_number: int, edges_number: int):
    generate_edges = list()
    edge = random.choices(range(vertices_number), k=2)

    while len(generate_edges) < edges_number:
        while edge[0] >= edge[1] or edge in generate_edges:
            edge = random.choices(range(vertices_number), k=2)
        generate_edges.append(edge)

    graph = np.zeros((vertices_number, vertices_number))
    for edge in generate_edges:
        graph[tuple(edge)] = 1
        
    return graph + np.transpose(graph)


def generate_N_P_graph(vertices_number: int, edges_probability: float):
    graph = np.random.choice([0, 1], (vertices_number, vertices_number), p=[1-edges_probability, edges_probability])
    graph = np.tril(graph, -1)
    return graph + np.transpose(graph)
