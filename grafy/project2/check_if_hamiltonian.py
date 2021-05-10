class WrongInputException(Exception):
    pass


# Global variable. True if given graph was hamiltonian. False by default.
is_hamiltonian = False

# Sample list from test script
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


def print_path(path: list):
    """
    Prints hamiltonian path into the terminal

        Parameters:
            path (list): possible path in hamiltonian graph

    """
    print('[ ', end='')
    for node in path:
        print(str(node+1) + ' -> ', end='')
    print(str(path[0]+1) + ' ]')


def check_if_hamiltonian(adj_list: dict, no_of_nodes: int, starting_node: int, visited_nodes: list, path: list):
    """
    Functions to check if graph is hamiltonian. Prints all possible paths

        Parameters:
            adj_list (dict): adjacency list
            no_of_nodes (int): number of nodes
            starting_node (int): starting node
            visited_nodes (list): list of visited nodes
            path (list): current path

    """
    global is_hamiltonian

    # Print path when all nodes have been visited and recently visited node connects to starting node
    if len(path) == no_of_nodes and path[0] in adj_list[path[no_of_nodes-1]]:
        is_hamiltonian = True
        print_path(path)

    # Loop through associated nodes
    for node in adj_list[starting_node]:

        if not visited_nodes[node]:
            visited_nodes[node] = True
            path.append(node)

            check_if_hamiltonian(adj_list, no_of_nodes, node, visited_nodes, path)

            visited_nodes[node] = False
            path.pop()


def check_number_of_nodes(adj_list: dict) -> int:
    """
    Check number of nodes in the graph.

        Parameters:
            adj_list (dict): adjacency list
        Returns:
            number of nodes (int)

    """
    if 0 > len(adj_list.keys()):
        return False
    return len(adj_list.keys())


def check_graph(adj_list: dict, starting_node=0):
    """
    Run function to check if given graph is hamiltonian.
    Prints all possible paths.

        Parameters:
            adj_list (dict): adjacency list
            starting_node (int): number of a starting node. Is 0 by default.

    """
    if type(adj_list) != dict:
        raise WrongInputException(f"Wrong input type of{type(adj_list)}. Should be dict")
    no_of_nodes = check_number_of_nodes(adj_list)

    if not no_of_nodes:
        raise WrongInputException("Number of nodes must be greater than 0")

    path = [starting_node]

    visited_nodes = [False]*no_of_nodes
    visited_nodes[starting_node] = True

    check_if_hamiltonian(adj_list, no_of_nodes, starting_node, visited_nodes, path)
    if not is_hamiltonian:
        print("Could not find any cycles, thus the graph is not hamiltonian")


