from graph_generation import generate_N_P_graph, generate_N_L_graph
from graph_visualization import visualize_graph
from graph_conversion import *

if __name__ == "__main__":
    graph_by_matrix = generate_N_L_graph(100, 5)
    visualize_graph(graph_by_matrix)