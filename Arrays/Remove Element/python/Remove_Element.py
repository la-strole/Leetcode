def remove_elements(array: list, value: int) -> int:
    """
    remove all value elements from array
    :param array: list of integers
    :param value: integer to remove
    :return: len of list: int
    """
    assert isinstance(array, list)
    for _ in array:
        assert isinstance(_, int)
    assert isinstance(value, int)

    while value in array:
        array.remove(value)
    return len(array)


if __name__ == '__main__':
    test_Array = [1, 2, 3, 4, 5, 61, 2, 3]
    element = 2
    print(f'len of array is {remove_elements(test_Array, element)}')
