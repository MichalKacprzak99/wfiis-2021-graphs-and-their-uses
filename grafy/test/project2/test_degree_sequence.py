import unittest

from grafy.project2.degree_sequence import degree_sequence_checker


class DegreeSequenceTest(unittest.TestCase):

    def test_degree_sequence_checker(self):

        with self.subTest():
            example_correct = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
            self.assertTrue(degree_sequence_checker(example_correct))

        with self.subTest():
            example_wrong = [6, 4, 3, 2, 2, 2, 1, 1]
            self.assertFalse(degree_sequence_checker(example_wrong))

        with self.subTest():
            example_wrong2 = [6, 5, 4, 3, 2, 1, 1]
            self.assertFalse(degree_sequence_checker(example_wrong2))

        with self.subTest():
            example_correct_from_lecture3 = [6, 4, 3, 3, 2, 2, 2]
            self.assertTrue(degree_sequence_checker(example_correct_from_lecture3))

        with self.subTest():
            example_correct_from_lecture0 = [4, 2, 3, 2, 3, 2]
            self.assertTrue(degree_sequence_checker(example_correct_from_lecture0))

        with self.subTest():
            example_wrong3 = [4, 4, 3, 3, 1, 2]
            self.assertFalse(degree_sequence_checker(example_wrong3))
