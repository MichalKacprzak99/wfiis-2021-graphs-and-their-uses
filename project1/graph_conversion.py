import numpy as np
from collections import defaultdict

graph_N_L = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
             [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
             [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]


def adj_matrix_to_list(adj_matrix):
    adjacency_list = defaultdict(list)
    for row in range(len(adj_matrix)):
        for col in range(len(adj_matrix)):
            if adj_matrix[row][col] == 1:
                adjacency_list[row].append(col + 1)

    return adjacency_list


def print_adj_list(adj_list):
    for row in adj_list:
        print(str(row + 1) + ": " + str(adj_list[row]))


def adj_list_to_matrix(adj_list):
    amount_of_keys = len(adj_list)
    adjacency_matrix = np.zeros((amount_of_keys, amount_of_keys))

    for key in adj_list:
        for value in adj_list[key]:
            adjacency_matrix[key][value - 1] = 1
            adjacency_matrix[value - 1][key] = 1

    return adjacency_matrix


def adj_matrix_to_inc_matrix(adj_matrix):
    number_of_edges = 0
    for row in adj_matrix:
        number_of_edges += np.count_nonzero(row == 1)
    number_of_edges = int(number_of_edges / 2)
    inc_matrix = np.zeros((len(adj_matrix), number_of_edges))

    current_edge = 0
    size = len(adj_matrix)
    for row in range(0, size):
        for col in range(row + 1, size):
            if adj_matrix[row][col]:
                inc_matrix[row][current_edge] = 1
                inc_matrix[col][current_edge] = 1
                current_edge += 1

    return inc_matrix


def inc_matrix_to_adj_matrix(inc_matrix):
    number_of_rows = len(inc_matrix)
    number_of_columns = len(inc_matrix[0])

    adj_matrix = np.zeros((number_of_rows, number_of_rows))
    for col in range(0, number_of_columns):

        start_of_edge = 0
        end_of_edge = 0

        for row in range(0, number_of_rows):
            if inc_matrix[row][col]:
                if start_of_edge == 0:
                    start_of_edge = row
                else:
                    end_of_edge = row
                    break

        adj_matrix[start_of_edge][end_of_edge] = 1
        adj_matrix[end_of_edge][start_of_edge] = 1

    return adj_matrix


def adj_list_to_inc_matrix(adj_list):
    adj_matrix = adj_list_to_matrix(adj_list)
    return adj_matrix_to_inc_matrix(adj_matrix)


def inc_matrix_to_adj_list(inc_matrix):
    adj_matrix = inc_matrix_to_adj_matrix(inc_matrix)
    return adj_matrix_to_list(adj_matrix)
