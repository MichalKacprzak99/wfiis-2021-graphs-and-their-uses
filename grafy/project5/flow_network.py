import numpy as np


def generate_flow_network(N: int) -> np.ndarray:
    """ Function generates random flow network with N layers between source and sink.
    Each edge has a random capacity in the range(1,10)

    Parameters
    ----------
    N : int
        number of layers in flow network(excluding source and sink)

    Returns
    -------
    np.ndarray
        graph representation of the flow network - in form of a adjacency matrix
    """
    layers = [1]

    for _ in range(N):
        layers.append(np.random.randint(2, N + 1))

    layers.append(1)

    last_node = 0
    nodes_in_layers = []
    for layer in layers:
        nodes_in_layers.append(list(range(last_node, layer + last_node)))
        last_node += layer

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

    graph = add_arcs_to_flow_network(graph, nodes_in_layers, 2 * N)
    graph = apply_capacity_to_flow_network(graph, 1, 10)
    return graph


# TODO - to fix
def add_arcs_to_flow_network(flow_network: np.ndarray, nodes_in_layers: list, k: int) -> np.ndarray:
    """ Function adds k random arcs to flow network

    Parameters
    ----------
    flow_network : np.ndarray
        flow network as adjacency matrix
    nodes_in_layers :
    k : int
        number of arcs to add
    Returns
    -------
    np.ndarray
        graph representation of the flow network - in form of a adjacency matrix
    """
    # random arcs
    graph_copy = flow_network.copy()
    graph_copy[0][-1] = 1
    graph_copy[-1][0] = 1
    np.fill_diagonal(graph_copy, 1)
    free_arcs = np.argwhere(graph_copy == 0)
    arcs_indices = np.random.choice(free_arcs.shape[0], size=k)
    arcs_to_add = free_arcs[arcs_indices]
    flow_network[tuple(np.transpose(arcs_to_add))] = 1

    # connecting only nodes in adjacent layers
    # nodes = list(range(1, graph.shape[0]-1))
    # while k != 0:
    #     arc_begin = np.random.choice(nodes, size=1)[0]
    #     for layer, nodes_in_layer in enumerate(nodes_in_layers[1:-1], start=1):
    #         if arc_begin in nodes_in_layer:
    #             possible_arc_ends = nodes_in_layers[layer - 1] + nodes_in_layers[layer + 1]
    #             possible_arc_ends = [node for node in possible_arc_ends if node not in [0, graph.shape[0]]]
    #             arcs = [(x, y) for x in [arc_begin] for y in possible_arc_ends if graph[x][y] != 1]
    #             if len(arcs) > 0:
    #                 arc_to_add = np.random.choice(len(arcs), size=1)[0]
    #                 print(graph[arcs[arc_to_add]])
    #                 graph[arcs[arc_to_add]] = 1
    #                 k -= 1
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
