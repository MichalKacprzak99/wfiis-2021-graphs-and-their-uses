import digraph_generation
import graph_conversion as gc
import numpy as np
import kosaraju

adj_matrix = [
    [0, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0]
]
adj_list = gc.adj_matrix_to_list(adj_matrix)
print(adj_list)
adj_matrix = np.array(adj_matrix)
kosaraju.kosaraju(adj_matrix)
