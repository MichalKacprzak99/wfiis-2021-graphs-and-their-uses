import unittest
import numpy as np


from project3.connected_graph_generation import generate_connected_graph


class ConnectedGraphGenerationTest(unittest.TestCase):

    def test_generate_N_L_graph_too_view_vertices(self):
        vertices_number = 0
        err_message = "The number of vertices must be positive"
        self.assertRaisesRegex(ValueError, err_message, generate_connected_graph, vertices_number)

    def test_generate_connected_graph_generated(self):
        vertices_number = 5

        graph_matrix = generate_connected_graph(vertices_number)

        with self.subTest():
            maximum_edges_number = (vertices_number * (vertices_number - 1) // 2)
            minimum_edges_number = vertices_number - 1
            generated_edges = np.count_nonzero(graph_matrix) // 2
            self.assertTrue(minimum_edges_number <= generated_edges <= maximum_edges_number)

        with self.subTest():
            is_diagonal_empty = False if np.sum(graph_matrix.diagonal()) else True
            self.assertTrue(is_diagonal_empty)

        with self.subTest():
            self.assertEqual(graph_matrix.tolist(), graph_matrix.T.tolist())