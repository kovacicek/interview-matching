import unittest
from algorithm_v1 import near_perfect_matches, validate


class TestAlgorithm(unittest.TestCase):
    def test_N_4(self):
        applicants = [[4, 3, 1, 2],
                      [2, 1, 3, 4],
                      [1, 3, 4, 2],
                      [4, 3, 1, 2]]

        apartments = [[3, 2, 4, 1],
                      [2, 3, 1, 4],
                      [3, 1, 2, 4],
                      [3, 2, 4, 1]]
        ret = near_perfect_matches(applicants, apartments)
        assert ret == [3, 2, 1, 4]

    def test_N_7(self):
        applicants = [
            [4, 5, 3, 7, 2, 6, 1],
            [5, 6, 4, 7, 3, 2, 1],
            [1, 6, 5, 4, 3, 7, 2],
            [3, 5, 6, 7, 2, 4, 1],
            [1, 7, 6, 4, 3, 5, 2],
            [6, 3, 7, 5, 2, 4, 1],
            [1, 7, 4, 2, 6, 5, 3]
        ]
        apartments = [
            [3, 4, 2, 1, 6, 7, 5],
            [6, 4, 2, 3, 5, 1, 7],
            [6, 3, 5, 7, 2, 4, 1],
            [1, 6, 3, 2, 4, 7, 5],
            [1, 6, 5, 3, 4, 7, 2],
            [1, 7, 3, 4, 5, 6, 2],
            [5, 6, 2, 4, 3, 7, 1]
        ]
        ret = near_perfect_matches(applicants, apartments)
        assert ret == [4, 3, 1, 5, 6, 2, 7]

    def test_stress_N_100(self):
        pass

    def test_stress_N_1000(self):
        pass

    def test_stress_N_10000(self):
        pass

    def test_validate_not_square_matrix(self):
        matrix = [[0, 1, 2, 3], [0, 1, 2, 3]]
        assert validate(matrix) is False

    def test_validate_matrix_not_integers(self):
        matrix = [[1, 2, 3], [1, 2, 3], ['a', 2, 3]]
        assert validate(matrix) is False

    def test_validate_matrix_integer_range(self):
        matrix = [[0, 2, 3], [1, 2, 3], [1, 2, 3]]
        assert validate(matrix) is False

    def test_validate_matrix_duplicates_in_row(self):
        matrix = [[1, 2, 2], [1, 2, 3], [1, 2, 3]]
        assert validate(matrix) is False

    def test_validate_pass(self):
        matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        assert validate(matrix)
