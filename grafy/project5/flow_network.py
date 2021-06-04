from itertools import islice

import numpy as np

from typing import List, Tuple


def generate_flow_network(N: int, min_capacity: int, max_capacity: int) -> Tuple[np.ndarray, List[list]]:
    """ Function generates random flow network with N layers between source and sink.
    Each edge has a random capacity in the range(1,10)

    Parameters
    ----------
    N : int
        positive number of layers in flow network(excluding source and sink)

    min_capacity : int
        minimum capacity of arc in flow network
    max_capacity : int
        maximum capacity of arc in flow network

    Returns
    -------
    Tuple[np.ndarray, List[list]]
        Tuple with graph representation of the flow network - in form of a adjacency matrix
        and layers of flow network
    """

    layers = [1]

    for _ in range(N):
        layers.append(np.random.randint(2, N + 1))

    layers.append(1)

    nodes_number = sum(layers)
    nodes = iter(range(nodes_number))
    nodes_in_layers = [list(islice(nodes, layer)) for layer in layers]

    graph = np.zeros((nodes_number, nodes_number), np.int)

    for layer, nodes in enumerate(nodes_in_layers[:-1]):
        for node in nodes:
            arcs_end = np.random.choice(nodes_in_layers[layer + 1], size=1)[0]
            graph[node][arcs_end] = 1

        for node in nodes_in_layers[layer + 1]:
            if np.sum(graph[:, node]) == 0:
                arcs_begin = np.random.choice(nodes, size=1)[0]
                graph[arcs_begin][node] = 1

    graph = add_arcs_to_flow_network(graph, 2 * N)
    graph = apply_capacity_to_flow_network(graph, min_capacity, max_capacity)
    return graph, nodes_in_layers


def add_arcs_to_flow_network(flow_network: np.ndarray, k: int) -> np.ndarray:
    """ Function adds k random arcs to flow network

    Parameters
    ----------
    flow_network : np.ndarray
        flow network as adjacency matrix
    k : int
        number of arcs to add
    Returns
    -------
    np.ndarray
        graph representation of the flow network - in form of a adjacency matrix
    """

    graph_copy = flow_network.copy()
    graph_copy[np.tril_indices(graph_copy.shape[0])] = -1

    free_arcs = np.argwhere(graph_copy == 0)

    arcs_indices = np.random.choice(free_arcs.shape[0], size=k)
    arcs_to_add = free_arcs[arcs_indices]

    def reverse_arc(arc, sink):

        if np.random.random() > 0.5 and arc[0] not in [0, sink-1]:
            return arc[::-1]
        else:
            return arc

    arcs_to_add = np.apply_along_axis(lambda arc: reverse_arc(arc, flow_network.shape[0]), 1, arcs_to_add)

    flow_network[tuple(np.transpose(arcs_to_add))] = 1

    return flow_network


def apply_capacity_to_flow_network(flow_network: np.ndarray, min_capacity: int, max_capacity: int) -> np.ndarray:
    """ Apply random capacity to each arc in flow network in range(min_capacity, max_capacity)

    Parameters
    ----------
    flow_network : np.ndarray
        flow network as adjacency matrix
    min_capacity : int
        minimum capacity of arc in flow network
    max_capacity : int
        maximum capacity of arc in flow network

    Returns
    -------
    np.ndarray
        graph representation of the flow network - in form of a adjacency matrix with applied capacity
    """

    def apply_capacity(edge):
        if edge == 1:
            return np.random.randint(min_capacity, max_capacity + 1)
        else:
            return edge

    apply_capacity = np.vectorize(apply_capacity)
    flow_network = apply_capacity(flow_network)

    return flow_network
