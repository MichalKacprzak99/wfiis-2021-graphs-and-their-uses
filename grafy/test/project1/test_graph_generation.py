import unittest
import numpy as np


from project1.graph_generation import generate_N_L_graph, generate_N_P_graph


class GraphGenerationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vertices_number = 1
        self.edges_number = 1

    def test_generate_N_L_graph_too_view_vertices(self):
        self.vertices_number = 0
        err_message = "The number of vertices must be positive"
        self.assertRaisesRegex(ValueError, err_message, generate_N_L_graph, self.vertices_number, self.edges_number)

    def test_generate_N_L_graph_too_many_edges(self):
        self.edges_number = 10
        err_message = f"The number of edges must be smaller than or equal to " \
                      f"{self.vertices_number * (self.vertices_number - 1) // 2} for {self.vertices_number} vertices"
        self.assertRaisesRegex(ValueError, err_message, generate_N_L_graph, self.vertices_number, self.edges_number)

    def test_generate_N_P_graph_wrong_probability(self):
        edges_probability = [-1, 2]
        err_message = "The probability value must be between 0 and 1"

        for p in edges_probability:
            with self.subTest():
                self.assertRaisesRegex(ValueError, err_message, generate_N_P_graph, self.vertices_number, p)

    def test_generate_N_L_graph_generated(self):
        self.vertices_number = 5
        self.edges_number = 10

        graph_matrix = generate_N_L_graph(self.vertices_number, self.edges_number)

        with self.subTest():
            generated_edges = np.count_nonzero(graph_matrix) // 2
            self.assertEqual(generated_edges, self.edges_number)

        with self.subTest():
            is_diagonal_empty = False if np.sum(graph_matrix.diagonal()) else True
            self.assertTrue(is_diagonal_empty)

        with self.subTest():
            self.assertEqual(graph_matrix.tolist(), graph_matrix.T.tolist())

    def test_generate_N_P_graph_generated(self):
        self.vertices_number = 5

        graph_matrix = generate_N_P_graph(self.vertices_number, 0.5)

        with self.subTest():
            maximum_edges_number = (self.vertices_number * (self.vertices_number - 1) // 2)
            minimum_edges_number = 0
            generated_edges = np.count_nonzero(graph_matrix) // 2
            self.assertTrue(minimum_edges_number <= generated_edges <= maximum_edges_number)

        with self.subTest():
            is_diagonal_empty = False if np.sum(graph_matrix.diagonal()) else True
            self.assertTrue(is_diagonal_empty)

        with self.subTest():
            self.assertEqual(graph_matrix.tolist(), graph_matrix.T.tolist())
