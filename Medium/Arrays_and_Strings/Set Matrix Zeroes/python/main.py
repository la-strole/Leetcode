from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        row_count = len(matrix)
        col_count = len(matrix[0])

        for row in range(row_count):
            for column in range(col_count):
                if matrix[row][column] == 0:
                    cols.add(column)
                    rows.add(row)

        for row in range(row_count):
            if row in rows:
                matrix[row] = [0] * col_count
            else:
                for col in cols:
                    matrix[row][col] = 0


if __name__ == "__main__":
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    print(matrix)
