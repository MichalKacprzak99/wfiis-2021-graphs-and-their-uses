from connected_graph_generation import generate_connected_graph
from dijkstra_algorithm import print_dijkstra_algorithm_result, dijkstra_algorithm
from project1.graph_visualization import visualize_graph
from graph_center import find_graph_center, find_graph_minimax_center, generate_vertices_distance_matrix


if __name__ == "__main__":

    random_connected_graph = generate_connected_graph(8)
    print("Adjacency matrix\n")
    print(random_connected_graph)

    distance_matrix, previous_matrix = dijkstra_algorithm(random_connected_graph)
    print()
    print_dijkstra_algorithm_result(distance_matrix, previous_matrix)
    vertices_distance_matrix = generate_vertices_distance_matrix(random_connected_graph)
    print("\nGraph distance matrix\n")
    print(vertices_distance_matrix)
    graph_center = find_graph_center(random_connected_graph)
    print(f"\nGraph center {graph_center}\n")
    graph_minimax_center = find_graph_minimax_center(random_connected_graph)
    print(f"Mnimax graph center: {graph_minimax_center}\n")
    visualize_graph(random_connected_graph)
