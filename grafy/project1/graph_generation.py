import numpy as np
import pretty_errors


def vertices_number_controller(graph_generator):
    def wrapper_vertices_number_controller(*args):
        vertices_number, _ = args
        if vertices_number <= 0:
            raise ValueError("The number of vertices must be positive")
        return graph_generator(*args)

    return wrapper_vertices_number_controller


@vertices_number_controller
def generate_N_L_graph(vertices_number: int, edges_number: int) -> np.ndarray:
    if edges_number > vertices_number * (vertices_number - 1) // 2:
        raise ValueError(f"The number of edges must be smaller than or equal "
                         f"to {vertices_number * (vertices_number - 1) // 2} for {vertices_number} vertices")

    generated_edges = 0
    graph = np.zeros((vertices_number, vertices_number))
    replace = vertices_number == 1

    while generated_edges < edges_number:
        edge = np.random.choice(range(vertices_number), size=2, replace=replace)
        if graph[tuple(edge)] == 0:
            graph[tuple(edge)] = 1
            graph[tuple(edge[::-1])] = 1
            generated_edges += 1
    return graph


@vertices_number_controller
def generate_N_P_graph(vertices_number: int, edges_probability: float) -> np.ndarray:
    if edges_probability < 0 or edges_probability > 1:
        raise ValueError("The probability value must be between 0 and 1")

    def random_edge(i, j):
        if i > j:
            return np.random.choice([0, 1], 1, p=[1 - edges_probability, edges_probability])
        else:
            return 0

    random_edge = np.vectorize(random_edge)
    graph = np.fromfunction(lambda i, j: random_edge(i, j), (vertices_number, vertices_number))

    return graph + np.transpose(graph)
