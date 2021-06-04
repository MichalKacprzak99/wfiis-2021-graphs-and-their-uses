import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from typing import List


def visualize_flow_network(flow_network: np.ndarray, layers: List[list], max_flow: np.ndarray = None):
    """ Visualize flow network with or without max flow in network

    Parameters
    ----------
    flow_network : np.ndarray
        flow network as adjacency matrix
    layers : List[list]
        structure of flow network
    max_flow : np.ndarray
        max flow in flow network as adjacency matrix
    """
    G = nx.from_numpy_array(flow_network, create_using=nx.MultiDiGraph)

    for layer_index, layer in enumerate(layers):
        for node in layer:
            G.nodes(data=True)[node]['layer'] = layer_index

    pos = nx.multipartite_layout(G, subset_key='layer')

    nx.draw(G, pos, with_labels=True, font_weight='bold')
    if max_flow is None:
        edge_labels = dict([((n1, n2), f'{flow_network[n1][n2]}')
                            for n1, n2, d in G.edges])
    else:
        edge_labels = dict([((n1, n2), f'{max_flow[n1][n2]}/{flow_network[n1][n2]}')
                            for n1, n2, d in G.edges])

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.6)
    plt.show()
