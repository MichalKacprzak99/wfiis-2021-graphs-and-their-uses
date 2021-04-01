# Kruskal's Minimum Spanning Tree algorithm using Union Find

# Sample graph with unsorted weights [src, dst, w]
sample_weighted_graph = [[0, 1, 3],
                         [0, 4, 9],
                         [0, 2, 2],
                         [1, 3, 2],
                         [1, 4, 4],
                         [2, 4, 6],
                         [2, 5, 9],
                         [3, 6, 3],
                         [4, 6, 1],
                         [4, 7, 2],
                         [5, 7, 1],
                         [5, 8, 2],
                         [6, 9, 5],
                         [7, 9, 5],
                         [7, 11, 9],
                         [7, 10, 6],
                         [8, 10, 2],
                         [9, 11, 5],
                         [10, 11, 3]]


# Neatly prints result graph in terminal
def print_result(tree):
    minimum_cost = 0
    print("Edges in the constructed tree")
    print("src --- w --- dst")
    for u, v, weight in tree:
        minimum_cost += weight
        print("%d --- %d --- %d" % (u+1, weight, v+1))
    print("Minimum Spanning Tree Cost =", minimum_cost)


# Find set of node i
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


# Unify two nodes
def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root

    else:
        parent[y_root] = x_root
        rank[x_root] += 1


# Kruskal algorithm for finding minimum spanning tree in graph
def kruskal_mst(graph, vertices):

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


# kruskal_mst(sample_weighted_graph, 12)
