import digraph_generation
import graph_conversion as gc
import kosaraju

adj_matrix = digraph_generation.generate_N_P_digraph(10, 0.1)
list = gc.adj_matrix_to_list(adj_matrix)
kosaraju.kosaraju(adj_matrix)

