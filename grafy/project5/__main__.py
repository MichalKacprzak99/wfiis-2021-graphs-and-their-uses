from grafy.project5.flow_network import generate_flow_network
from grafy.project1.graph_visualization import visualize_graph


def print_array(arr):
    """
    prints a 2-D numpy array in a nicer format
    """
    for a in arr:
        for elem in a:
            print(f"{elem:<2.0f}".rjust(3), end="")
        print(end="\n")


if __name__ == '__main__':
    flow_network = generate_flow_network(N=2)
    print("Flow network as adjacency matrix:\n")
    print_array(flow_network)
    visualize_graph(flow_network, weighted_graph=True, digraph=True)
