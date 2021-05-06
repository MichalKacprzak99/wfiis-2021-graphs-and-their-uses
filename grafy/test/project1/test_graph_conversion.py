import unittest

from project1.graph_conversion import *


class TestGraphConversion(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.adj_matrix = np.asarray([[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
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
                                     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]])

        cls.adj_list = defaultdict(list, {0: [1, 4, 5],
                                          1: [0, 2, 5],
                                          2: [1, 3, 4, 11],
                                          3: [2, 7, 8, 10],
                                          4: [0, 2, 6, 8],
                                          5: [0, 1, 6], 6: [4, 5, 7],
                                          7: [3, 6, 8, 11],
                                          8: [3, 4, 7, 9], 9: [8],
                                          10: [3], 11: [2, 7]
                                          })

        cls.inc_matrix = np.asarray([[1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                     [1., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                     [0., 0., 0., 1., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                                     [0., 0., 0., 0., 0., 1., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0.],
                                     [0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0.],
                                     [0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
                                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 1., 0., 0., 0.],
                                     [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 1., 1., 0.],
                                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.],
                                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                                     [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]])

    def test_conversion_adj_matrix_to_adj_list(self):
        converted_adj_list = adj_matrix_to_list(self.adj_matrix)
        self.assertEqual(converted_adj_list, self.adj_list)

    def test_conversion_adj_list_to_adj_matrix(self):
        converted_adj_matrix = adj_list_to_matrix(self.adj_list)
        self.assertTrue(np.array_equal(converted_adj_matrix, self.adj_matrix))

    def test_conversion_inc_matrix_to_adj_matrix(self):
        converted_adj_matrix = inc_matrix_to_adj_matrix(self.inc_matrix)
        self.assertTrue(np.array_equal(converted_adj_matrix, self.adj_matrix))

    def test_conversion_adj_matrix_to_inc_matrix(self):
        converted_inc_matrix = adj_matrix_to_inc_matrix(self.adj_matrix)
        self.assertTrue(np.array_equal(converted_inc_matrix, self.inc_matrix))

    def test_conversion_adj_list_to_inc_matrix(self):
        converted_inc_matrix = adj_list_to_inc_matrix(self.adj_list)
        self.assertTrue(np.array_equal(converted_inc_matrix, self.inc_matrix))

    def test_conversion_inc_matrix_to_adj_list(self):
        converted_adj_list = inc_matrix_to_adj_list(self.inc_matrix)
        self.assertTrue(converted_adj_list, self.adj_list)
