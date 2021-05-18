class WrongInputException(Exception):
    pass


def validate_adjacency_matrix(matrix: list) -> bool:
    """
    Validate the input matrix.

        Parameters:
            Adjacency matrix (list): Adjacency matrix graph representation

        Returns:
            valid (bool): True if matrix is valid, False if not
    """
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if not matrix[i][j] == matrix[j][i]:
                return False
    return True


def convert_adj_matrix(matrix: list) -> list:
    """
    Convert adjacency matrix to suitable list representation

        Parameters:
            Adjacency matrix (list): Adjacency matrix graph representation

        Returns:
            Graph (list): Weighted graph representation

    """
    graph = []
    size = len(matrix)
    curr = -1
    for row in matrix:
        curr += 1
        for i in range(curr, size):
            if row[i] != 0:
                graph.append([curr, i, row[i]])

    return graph


def get_vertices(graph: list) -> int:
    """
    Get number of vertices in a graph

        Parameters:
            graph (list): weighted graph list representation

        Returns:
            vertices (int): number of vertices in given graph
    """
    vertices = 0
    for n in graph:
        if vertices <= n[0]:
            vertices = n[0]
        if vertices <= n[1]:
            vertices = n[1]
    return vertices+1


def print_result(tree: list) -> None:
    """
    Prints MST results

        Parameters:
            tree (list): Minimum Spanning Tree

        Returns:
            None
    """
    minimum_cost = 0
    print("Edges in the constructed tree")
    print("src --- w --- dst")
    for u, v, weight in tree:
        minimum_cost += weight
        print(str(u+1).rjust(3, ' ') + '   <--- ' + str(weight).rjust(3, ' ') + '   ---> ' + str(v+1).rjust(3, ' '))
    print("Minimum Spanning Tree Cost =", minimum_cost)


def find(parent: list, i: int) -> int:
    """
    Find set of node i

        Parameters:
            parent (list): list of i-th node parents
            i (int): i-th node

        Returns:
            i-th node root node
    """
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent: list, rank: list, x: int, y: int) -> None:
    """
    Unify sets of lists of nodes. Union-Find algorithm.

        Parameters:
            parent (list): list of parent nodes
            rank (list): ranking list
            x (int): first given node
            y (int): second given node

        Returns:
            None
    """
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root

    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def kruskal_mst(adjacency_matrix: list) -> None:
    """
    Kruskal algorithm for finding minimum spanning tree.
    Prints the resulting tree information in terminal.

        Parameters:
            adjacency_matrix (list): adjacency matrix graph representation

        Returns:
            None
    """
    if not validate_adjacency_matrix(adjacency_matrix):
        raise WrongInputException("Wrong input matrix")

    graph = convert_adj_matrix(adjacency_matrix)

    vertices = get_vertices(graph)
    if vertices <= 0:
        raise WrongInputException('Number of vertices must be greater than 0')

    g_size = len(graph)  # graph list size
    result_tree = []    # result_tree tree
    parent = []         # array of roots
    rank = []           # rank array
    i = 0               # index var for sorted edges
    e = 0               # index var for result_tree tree

    # Sorting the graph by weight (ascending)
    graph = sorted(graph, key=lambda l: l[2])

    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    while e < vertices - 1:

        if i == g_size:
            raise WrongInputException("Cannot create MST, check your input")

        src = graph[i][0]
        dst = graph[i][1]
        w = graph[i][2]

        i = i + 1

        x = find(parent, src)
        y = find(parent, dst)

        if x != y:
            e = e + 1
            result_tree.append([src, dst, w])
            union(parent, rank, x, y)

    print_result(result_tree)


def test_kruskal_mst() -> None:
    """
    Test kruskal MST with sample data
    """

    # sample_weighted_graph = [[0, 1, 3],
    #                          [0, 4, 9],
    #                          [0, 2, 2],
    #                          [1, 3, 2],
    #                          [1, 4, 4],
    #                          [2, 4, 6],
    #                          [2, 5, 9],
    #                          [3, 6, 3],
    #                          [4, 6, 1],
    #                          [4, 7, 2],
    #                          [5, 7, 1],
    #                          [5, 8, 2],
    #                          [6, 9, 5],
    #                          [7, 9, 5],
    #                          [7, 11, 9],
    #                          [7, 10, 6],
    #                          [8, 10, 2],
    #                          [9, 11, 5],
    #                          [10, 11, 3]]

    sample_adjacency_matrix = [[0, 3, 2, 0, 9, 0, 0, 0, 0, 0, 0, 0],
                               [3, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0],
                               [2, 0, 0, 0, 6, 9, 0, 0, 0, 0, 0, 0],
                               [0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
                               [9, 4, 6, 0, 0, 0, 1, 2, 0, 0, 0, 0],
                               [0, 0, 9, 0, 0, 0, 0, 1, 2, 0, 0, 0],
                               [0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 0, 0],
                               [0, 0, 0, 0, 2, 1, 0, 0, 0, 5, 6, 9],
                               [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
                               [0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 5],
                               [0, 0, 0, 0, 0, 0, 0, 6, 2, 0, 0, 3],
                               [0, 0, 0, 0, 0, 0, 0, 9, 0, 5, 3, 0]]

    kruskal_mst(sample_adjacency_matrix)

