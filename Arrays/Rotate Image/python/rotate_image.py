import numpy


def rotate(matrix: list) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    matrix[:] = numpy.rot90(matrix, axes=(1, 0)).tolist()


if __name__ == "__main__":
    test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # expected output is [[7,4,1],[8,5,2],[9,6,3]]
    rotate(test_matrix)
    print(f"turned 90 deg matrix is {test_matrix}")
