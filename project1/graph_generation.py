import numpy as np


def generate_N_L_graph(vertices_number: int, edges_number: int):
    generated_edges = 0
    graph = np.zeros((vertices_number, vertices_number))
    edge = np.random.choice(vertices_number, size=2, replace=False)
    while generated_edges < edges_number:
        while graph[tuple(edge)] == 1:
            edge = np.random.choice(range(vertices_number), size=2, replace=False)

        graph[tuple(edge)] = 1
        graph[tuple(edge[::-1])] = 1
        generated_edges += 1

    return graph


def generate_N_P_graph(vertices_number: int, edges_probability: float):
    graph = np.random.choice([0, 1], (vertices_number, vertices_number),
                             p=[1-edges_probability, edges_probability], replace=False)
    graph = np.tril(graph, -1)
    return graph + np.transpose(graph)
