import numpy as np
from collections import defaultdict


def adj_matrix_to_list(adj_matrix):
    adjacency_list = defaultdict(list)

    for index, item in np.ndenumerate(adj_matrix):
        row, column = index
        if item == 1:
            adjacency_list[row].append(column)

    return adjacency_list


def print_adj_list(adj_list):
    for row in adj_list:
        print(str(row + 1) + ": " + str(list(map(lambda vertex: vertex + 1, adj_list[row]))))


def adj_list_to_matrix(adj_list):
    amount_of_keys = len(adj_list)
    adjacency_matrix = np.zeros((amount_of_keys, amount_of_keys))

    for key, row in adj_list.items():
        for item in row:
            adjacency_matrix[key][item] = 1
            adjacency_matrix[item][key] = 1

    return adjacency_matrix


def adj_matrix_to_inc_matrix(adj_matrix):
    number_of_edges = 0
    for row in adj_matrix:
        number_of_edges += np.count_nonzero(row == 1)
    number_of_edges = int(number_of_edges / 2)
    inc_matrix = np.zeros((len(adj_matrix), number_of_edges))

    current_edge = 0
    size = len(adj_matrix)

    for row_index, row in enumerate(adj_matrix):
        for col_index in range(row + 1, size):
            if row[col_index]:
                inc_matrix[row_index][current_edge] = 1
                inc_matrix[col_index][current_edge] = 1
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

