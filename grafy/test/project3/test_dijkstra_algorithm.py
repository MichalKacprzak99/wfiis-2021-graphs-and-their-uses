import unittest
import numpy as np

from project3.dijkstra_algorithm import dijkstra_algorithm, generate_shortest_paths


class DijkstraAlgorithmTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.graph_matrix_test = np.array([[0, 8, 0, 9, 3, 9, 5],
                                          [8, 0, 0, 2, 4, 0, 1],
                                          [0, 0, 0, 0, 0, 4, 0],
                                          [9, 2, 0, 0, 0, 9, 0],
                                          [3, 4, 0, 0, 0, 4, 0],
                                          [9, 0, 4, 9, 4, 0, 0],
                                          [5, 1, 0, 0, 0, 0, 0]])

        cls.d_table_test = [0, 6, 11, 8, 3, 7, 5]
        cls.p_table_test = [None, 6, 5, 1, 0, 4, 0]

        cls.shortest_paths_test = [[1], [1, 7, 2], [1, 5, 6, 3], [1, 7, 2, 4], [1, 5], [1, 5, 6], [1, 7]]



    def test_dijkstra_algorithm_wrong_vertex_number(self):
        vertices_number, _ = self.graph_matrix_test.shape

        start_vertices = [0, vertices_number + 1]
        err_message = f"Value of start vertex must be between 1 and {vertices_number}"
        for start_vertex in start_vertices:
            with self.subTest():
                self.assertRaisesRegex(ValueError, err_message, dijkstra_algorithm, self.graph_matrix_test,
                                       start_vertex)

    def test_dijkstra_algorithm_negative_weight(self):
        pass

    def test_dijkstra_algorithm_tables_generated(self):
        d_table, p_table = dijkstra_algorithm(self.graph_matrix_test)
        with self.subTest():
            self.assertEqual(p_table, self.p_table_test)

        with self.subTest():
            self.assertEqual(d_table, self.d_table_test)

    def test_shortest_paths_generated(self):
        _, p_table = dijkstra_algorithm(self.graph_matrix_test)
        generated_paths = generate_shortest_paths(p_table)
        self.assertEqual(generated_paths, self.shortest_paths_test)
