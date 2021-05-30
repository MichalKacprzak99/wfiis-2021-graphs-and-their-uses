from grafy.project5.flow_network import generate_flow_network
from grafy.project5.ford_fulkerson import ford_fulkerson
from grafy.project1.graph_visualization import visualize_graph

if __name__ == '__main__':
    flow_network = generate_flow_network(2)
    print(flow_network)
    visualize_graph(flow_network, True, True)
    # max_flow_network = ford_fulkerson(flow_network, 0, 5)
    # visualize_graph(max_flow_network, T
