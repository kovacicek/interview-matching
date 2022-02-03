import numpy as np


def transpose_matrix(matrix):
    zipped_rows = zip(*matrix)
    transposed_matrix = [list(row) for row in zipped_rows]
    return transposed_matrix


def weight_matrix(matrix, transpose=False):
    """
    Add weight to preference in terms that last row has weight 1.
    Moving to left (higher preference) weight is increasing by 1.

    Rearrange matrix in form:
    apl \ app
      1 2 3 4
    1
    2
    3
    4
    Convert Matrix to weighted matrix.
      :param matrix:      Matrix (list of lists)
    :param transpose:   Bool
    :return:            Matrix
    """
    dimension = len(matrix)
    weighted_matrix = [[1]] * dimension
    for row_index, row in enumerate(matrix):
        weighted_row = [1] * dimension
        for j, index in enumerate(row):
            weighted_row[index-1] = dimension - j
        weighted_matrix[row_index] = weighted_row
    return weighted_matrix if not transpose else transpose_matrix(weighted_matrix)


def near_perfect_matches(apl, app):
    w_apl = np.array(weight_matrix(apl))
    w_app = np.array(weight_matrix(app, transpose=True))
    weighted_sum = w_apl * w_app
    print(weighted_sum)

    # How to continue

    # machine learning approach
    # idea is to generate combination for which sum will be the greatest
    # maybe using classification and in that case normalize matrix by dividing by NxN

    # if machine learning is not used
    # start from picking the highest products in matrix
    # first test case will return
    # [[2  2  9  4]
    #  [9 16  4  3]
    #  [16 3 12  8]
    #  [4  1  3  8]
    # i.e. in first test case first pick 16 from position 2, 0
    # eliminate row 2 and column 0 and continue the process

    return weighted_sum


if __name__ == '__main__':
    applicants = [[4, 3, 1, 2],
                  [2, 1, 3, 4],
                  [1, 3, 4, 2],
                  [4, 3, 1, 2]]

    apartments = [[3, 2, 4, 1],
                  [2, 3, 1, 4],
                  [3, 1, 2, 4],
                  [3, 2, 4, 1]]
    ret = near_perfect_matches(applicants, apartments)
