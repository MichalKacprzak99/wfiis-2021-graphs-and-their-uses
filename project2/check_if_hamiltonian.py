# Sample from test script
sample_adj_list = {
            0: [1, 3, 4],
            1: [0, 2, 4, 5],
            2: [1, 3, 6],
            3: [0, 2, 5, 6],
            4: [0, 1, 7],
            5: [1, 3, 7],
            6: [2, 3, 7],
            7: [4, 5, 6]
}


# Neatly print path taken throughout the graph
def print_path(path):

    print('[ ', end='')
    for node in path:
        print(str(node+1) + ' -> ', end='')
    print(str(path[0]+1) + ' ]')


# Core function - checking if graph is hamiltonian, if so prints possible paths
def check_if_hamiltonian(adj_list, no_of_nodes, starting_node, visited_nodes, path):

    # Print path when all nodes have been visited and recently visited node connects to starting node
    if len(path) == no_of_nodes and path[0] in adj_list[path[no_of_nodes-1]]:
        print_path(path)

    # Loop through associated nodes
    for node in adj_list[starting_node]:

        if not visited_nodes[node]:
            visited_nodes[node] = True
            path.append(node)

            check_if_hamiltonian(adj_list, no_of_nodes, node, visited_nodes, path)

            visited_nodes[node] = False
            path.pop()


# Check if graph is small - eight nodes max
def check_number_of_nodes(adj_list):
    if 0 > len(adj_list.keys()) > 8:
        return False
    return len(adj_list.keys())


# Run function, default starting node is 0
def run(adj_list, starting_node=0):

    # Total number of nodes in the graph
    no_of_nodes = check_number_of_nodes(adj_list)

    # Reality check
    if not no_of_nodes:
        exit()

    # Path taken - starting from the starting node
    path = [starting_node]

    # Visited nodes - starting node is visited by default
    visited_nodes = [False]*no_of_nodes
    visited_nodes[starting_node] = True

    # Curtain raises
    check_if_hamiltonian(adj_list, no_of_nodes, starting_node, visited_nodes, path)


# run(sample_adj_list)
