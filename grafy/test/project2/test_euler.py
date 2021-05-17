import unittest
import numpy as np
from grafy.project2.check_if_euler import print_euler_cycle, get_euler_graph


class CheckIfEulerTest(unittest.TestCase):

    def test_negative_amount_of_vertices_get_euler_graph(self):
        amount_of_vertices = -3
        err_message = "N has to be greater than 0"
        self.assertRaisesRegex(ValueError, err_message, get_euler_graph, amount_of_vertices)

    def test_no_vertices_get_euler_graph(self):
        amount_of_vertices = 0
        err_message = "N has to be greater than 0"
        self.assertRaisesRegex(ValueError, err_message, get_euler_graph, amount_of_vertices)

    def test_positive_amount_of_vertices_get_euler_graph(self):
        amount_of_vertices = 2
        is_generated = len(get_euler_graph(amount_of_vertices)) > 0
        self.assertTrue(is_generated)



