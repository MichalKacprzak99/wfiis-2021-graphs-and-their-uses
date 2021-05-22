import itertools
from pprint import pprint

import numpy as np


def generate_flow_network(N: int) -> np.ndarray:
    layers = [1]
    for _ in range(N):
        layers.append(np.random.randint(2, N + 1))
    layers.append(1)
    last_node = 0
    nodes_in_layers = []
    for layer in layers:
        nodes = []
        for node in range(last_node, layer + last_node):
            nodes.append(node)
        nodes_in_layers.append(nodes)
        last_node = nodes[-1] + 1

    nodes_number = sum(layers)
    graph = np.zeros((nodes_number, nodes_number), np.int)

    for layer, nodes_in_layer in enumerate(nodes_in_layers[:-1]):
        for node in nodes_in_layer:
            arcs_end = np.random.choice(nodes_in_layers[layer + 1], size=1)[0]
            graph[node][arcs_end] = 1

        for node in nodes_in_layers[layer + 1]:
            if np.sum(graph[:, node]) == 0:
                arcs_begin = np.random.choice(nodes_in_layer, size=1)[0]
                graph[arcs_begin][node] = 1

    pprint(graph)
    graph = add_arcs_to_flow_network(graph, nodes_in_layers, 2 * N)
    graph = apply_capacity_to_flow_network(graph, 1, 10)
    return graph


def add_arcs_to_flow_network(graph: np.ndarray, nodes_in_layers: list, k: int) -> np.ndarray:
    nodes = list(range(1, graph.shape[0]-1))
    while k != 0:
        arc_begin = np.random.choice(nodes, size=1)[0]
        for layer, nodes_in_layer in enumerate(nodes_in_layers[1:-1], start=1):
            if arc_begin in nodes_in_layer:
                possible_arc_ends = nodes_in_layers[layer - 1] + nodes_in_layers[layer + 1]
                possible_arc_ends = [node for node in possible_arc_ends if node not in [0, graph.shape[0]]]
                arcs = [(x, y) for x in [arc_begin] for y in possible_arc_ends if graph[x][y] != 1]
                if len(arcs) > 0:
                    arc_to_add = np.random.choice(len(arcs), size=1)[0]
                    graph[arcs[arc_to_add]] = 1
                    k -= 1
    return graph


def apply_capacity_to_flow_network(graph: np.ndarray, min_capacity, max_capacity) -> np.ndarray:
    def apply_capacity(edge):
        if edge == 1:
            return np.random.randint(min_capacity, max_capacity + 1)
        else:
            return edge

    apply_capacity = np.vectorize(apply_capacity)
    graph = apply_capacity(graph)

    return graph
