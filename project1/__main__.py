from graph_generation import generate_N_P_graph, generate_N_L_graph
from graph_visualization import visualize_graph


if __name__ == "__main__":
    visualize_graph(generate_N_L_graph(5, 5))
