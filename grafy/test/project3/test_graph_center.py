import unittest
import numpy as np
from grafy.project3.graph_center import find_graph_center, find_graph_minimax_center, generate_vertices_distance_matrix


class GraphCenterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.graph_matrix_test = np.array([[0, 8, 0, 9, 3, 9, 5],
                                          [8, 0, 0, 2, 4, 0, 1],
                                          [0, 0, 0, 0, 0, 4, 0],
                                          [9, 2, 0, 0, 0, 9, 0],
                                          [3, 4, 0, 0, 0, 4, 0],
                                          [9, 0, 4, 9, 4, 0, 0],
                                          [5, 1, 0, 0, 0, 0, 0]])

        cls.vertices_distance_matrix_test = np.asarray([[0., 6., 11., 8., 3., 7., 5.],
                                                        [6., 0., 12., 2., 4., 8., 1.],
                                                        [11., 12., 0., 13., 8., 4., 13.],
                                                        [8., 2., 13., 0., 6., 9., 3.],
                                                        [3., 4., 8., 6., 0., 4., 5.],
                                                        [7., 8., 4., 9., 4., 0., 9.],
                                                        [5., 1., 13., 3., 5., 9., 0.]])

    def test_generated_vertices_distance_matrix(self):
        generated_vertices_distance_matrix = generate_vertices_distance_matrix(self.graph_matrix_test)
        self.assertTrue(np.array_equal(generated_vertices_distance_matrix, self.vertices_distance_matrix_test))

    def test_graph_center(self):
        graph_center_test = 5
        graph_center = find_graph_center(self.graph_matrix_test)
        self.assertEqual(graph_center, graph_center_test)

    def test_graph_minimax_center(self):
        graph_minimax_center_test = 5
        graph_minimax_center = find_graph_minimax_center(self.graph_matrix_test)
        self.assertEqual(graph_minimax_center, graph_minimax_center_test)

