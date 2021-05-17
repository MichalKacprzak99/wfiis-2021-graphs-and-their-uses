import unittest
from grafy.project2.graph_randomization import randomize_graph, generate_regular_graph, \
    create_graph_from_degree_sequence
from grafy.project2.degree_sequence import degree_sequence_checker


class GraphRandomizationTest(unittest.TestCase):

    def test_creating_graph_from_correct_degree_sequence(self):
        degree_sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
        self.assertTrue(degree_sequence_checker(degree_sequence))
        is_generated = len(create_graph_from_degree_sequence(degree_sequence)) > 0
        self.assertTrue(is_generated)

    def test_graph_randomization_from_correct_degree_sequence(self):
        degree_sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
        self.assertTrue(degree_sequence_checker(degree_sequence))
        graph = create_graph_from_degree_sequence(degree_sequence)
        random_graph = randomize_graph(degree_sequence, 2)
        self.assertNotEqual(graph, random_graph)

    def test_generating_regular_graph(self):
        generate_regular_graph(7, 2)
