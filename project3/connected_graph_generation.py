import numpy as np
from project1.graph_generation import generate_N_L_graph
from project1.graph_visualization import visualize_graph


def generate_connected_graph(vertices_number: int) -> np.ndarray:
    edges_number = ((vertices_number - 1) * (vertices_number - 2) // 2) + 1
    connected_graph = generate_N_L_graph(vertices_number, edges_number)

    def apply_weight(edge):

        if edge == 1:
            return np.random.randint(1, 11)
        else:
            return edge

    apply_weight = np.vectorize(apply_weight)
    return apply_weight(connected_graph)
