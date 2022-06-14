def best_deal(array: list) -> int:
    """
    get array as a list of prices, return best margin
    :param array: array: list of int
    :return: best margin: int
    """

    margin = 0
    valley = array[0]

    for vertex in range(1, len(array)):
        if array[vertex] < valley:
            valley = array[vertex]
            continue
        else:
            peak = array[vertex]
            margin += peak - valley
            valley = peak
    return margin


if __name__ == "__main__":
    assert best_deal([6, 1, 3, 2, 4, 7]) == 7
    assert best_deal([7, 1, 5, 3, 6, 4]) == 7
    assert best_deal([1, 2, 3, 4, 5]) == 4
    print("test passed")
