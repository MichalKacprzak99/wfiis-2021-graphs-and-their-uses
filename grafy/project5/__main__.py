from grafy.project5.flow_network import generate_flow_network
from grafy.project5.ford_fulkerson import ford_fulkerson
from grafy.project5.visualize_flow_network import visualize_flow_network


def print_array(arr):
    """
    prints a 2-D numpy array in a nicer format
    """
    for a in arr:
        for elem in a:
            print(f"{elem:<2.0f}".rjust(3), end="")
        print(end="\n")


if __name__ == '__main__':
    flow_network, layers = generate_flow_network(N=0)
    print("Flow network as adjacency matrix:\n")
    print_array(flow_network)

    max_flow_network = ford_fulkerson(flow_network, 0, 5)
    print("Max Flow in network as adjacency matrix:\n")
    print_array(flow_network)

    visualize_flow_network(flow_network, layers)

