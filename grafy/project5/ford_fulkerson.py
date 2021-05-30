sample_graph = [[0, 10, 5, 0, 0, 0],
 [0, 0, 0, 9, 4, 0],
 [0, 0, 0, 2, 0, 0],
 [0, 0, 0, 0, 3, 9],
 [0, 8, 0, 0, 0, 9],
 [0, 0, 0, 1, 4, 0]]


def bfs(graph, row, s, t, parent):
    """
      BFS algorithm for fining shortest path between two nodes.

           Parameters:
               graph (list): matrix representation of generated flow network
               row (int): matrix row size
               s (int): flow network's source
               t (int): flow network's sink
               parent (list): parent list

           Returns:
               Boolean
       """
    visited = [False] * row
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def ford_fulkerson(graph, source, sink):
    """
        Ford-Fulkerson's algorithm.
        Prints Max Flow into terminal.

           Parameters:
               graph (list): matrix representation of generated flow network
               source (int): flow network's source
               sink (int): flow network's sink

           Returns:
               graph (list): modified matrix representation of flow network
    """
    row = len(graph)
    parent = [-1] * row
    max_flow = 0

    while bfs(graph, row, source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    print("Max flow: %d" % max_flow)
    return graph


def test_ford_fulkerson_algo():
    """
      Test Ford-Fulkerson's algorithm.
      Executes the algorithm using sample data.
    """
    source = 0
    sink = 5
    print(ford_fulkerson(sample_graph, source, sink))
    print(sample_graph)

# test_ford_fulkerson_algo()