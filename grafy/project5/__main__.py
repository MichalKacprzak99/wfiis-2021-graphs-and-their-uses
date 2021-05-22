from grafy.project5.flow_network import generate_flow_network
from grafy.project1.graph_visualization import visualize_graph
if __name__ == '__main__':
    flow_network = generate_flow_network(2)
    print(flow_network)
    visualize_graph(flow_network, True, True)