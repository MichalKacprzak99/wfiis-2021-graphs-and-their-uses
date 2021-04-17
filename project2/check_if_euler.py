# First:
# take the n variable
# create a degree sequence
# generate a regular graph
# randomize that graph until you get a euler cycle
# if euler cycle received, list that euler cycle
from random import randint
from graph_randomization import create_graph_from_degree_sequence
from project1.graph_visualization import visualize_graph
from project1.graph_conversion import adj_list_to_matrix
from typing import List, DefaultDict
import copy


# Function converting a graph into a list
# TODO: Change this function into a different one maybe
def convert_graph(graph: DefaultDict[int, list]) -> List:
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((u, v))
    return edges


# Function checking if an edge is a bridge
# A bridge is an edge that connects two parts of the graph
def is_bridge(graph: DefaultDict[int, list]) -> int:
    start = list(graph)[0]
    visited = {}

    for v in graph:
        visited[v] = -1
    visited[start] = 0
    S = [start]
    while len(S) != 0:
        u = S.pop()
        for v in graph[u]:
            if v in visited and visited[v] == -1:
                visited[v] = 0
                S.append(v)
            visited[u] = 1
    return list(visited.values()).count(1) != len(graph)


# A function generating a graph based on the number for edges specified
# TODO: Change the convert_graph in while into a variable that is being updated throughout the loop
def get_euler_graph(n: int) -> List:
    degree_sequence = [randint(1, int(n / 2)) * 2 for x in range(n)]

    graph_adj_list = create_graph_from_degree_sequence(degree_sequence)
    visualize_graph(adj_list_to_matrix(graph_adj_list))

    graph_copy = copy.copy(graph_adj_list)
    euler_cycle = []
    u = list(graph_copy.keys())[0]

    while len(convert_graph(graph_copy)) > 0:
        current_vertex = u
        for u in list(graph_copy[current_vertex]):
            graph_copy[current_vertex].remove(u)
            graph_copy[u].remove(current_vertex)

            bridge = is_bridge(graph_copy)
            if bridge:
                graph_copy[current_vertex].append(u)
                graph_copy[u].append(current_vertex)
            else:
                break
        if bridge:
            if u in graph_copy[current_vertex]:
                graph_copy[current_vertex].remove(u)
            if current_vertex in graph_copy[u]:
                graph_copy[u].remove(current_vertex)
            graph_copy.pop(current_vertex)
        euler_cycle.append((current_vertex, u))

    return euler_cycle


# Print euler cycle
# Add 1 to vertex numbers
def print_euler_cycle(array: List) -> None:
    result = ''.join('%s->' % str(x[0] + 1) for x in array)
    result += str(array[-1][1] + 1)
    print(result)


euler = get_euler_graph(5)
print_euler_cycle(euler)

