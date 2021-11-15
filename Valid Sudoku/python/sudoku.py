def isValidSudoku(board) -> bool:
    """
    Return if this sudoku board is valid
    :param board: board - list of list of char 90-9 or .
    :return: True or False
    """

    assert isinstance(board, list)
    assert len(board) == 9
    for row in board:
        assert isinstance(row, list)
        assert len(row) == 9

    #

    def is_valid_block(block: list):
        """
        Return if block of 9 elements is valid sudoku block
        (it can consists of '1` - `9` without duplication and multiple number of '.'
        :param block: list, length = 9
        :return: True or False
        """
        assert isinstance(block, list)
        assert len(block) == 9, f"AssertionError: length of block {block} is not 9"

        for i, element in enumerate(block):
            if element == '.':
                continue
            elif element in block[i + 1:]:
                return False
        return True

    def sub_box_generator(board: list):
        """
        Return 3x3 sudoku sub-box.
        :param i: top-left element row
        :param j: top-left element column
        :param board - list of list sudoku board
        :return: 9 element array - sudoku sub_box
        """
        i_matrix = [0, 0, 0, 3, 3, 3, 6, 6, 6]
        j_matrix = [0, 3, 6, 0, 3, 6, 0, 3, 6]

        for i, j in zip(i_matrix, j_matrix):
            sub_box = []
            for row in range(i, i + 3):
                for column in range(j, j + 3):
                    sub_box.append(board[row][column])
            yield sub_box

    # check columns
    for column in range(9):
        block = [board[i][column] for i in range(9)]
        if not is_valid_block(block):
            return False
    # check rows
    for row in range(9):
        if not is_valid_block(board[row]):
            return False
    # check 3x3 blocks
    sub_block = sub_box_generator(board)
    for _ in range(9):
        if not is_valid_block(next(sub_block)):
            return False

    return True


if __name__ == "__main__":
    test_board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
                  [".", "4", ".", "3", ".", ".", ".", ".", "."],
                  [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                  ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                  [".", ".", "2", ".", "7", ".", ".", ".", "."],
                  [".", "1", "5", ".", ".", ".", ".", ".", "."],
                  [".", ".", ".", ".", ".", "2", ".", ".", "."],
                  [".", "2", ".", "9", ".", ".", ".", ".", "."],
                  [".", ".", "4", ".", ".", ".", ".", ".", "."]]

    print(f"test_board sudoku mattrix valid is {isValidSudoku(test_board)}")
