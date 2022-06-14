def twoSum(nums: list, target: int) -> list:
    """
    Return pair from integers from nums wich sum is target
    :param nums: list of integers
    :param target: integer
    :return: list of two integers
    """

    assert isinstance(nums, list)
    assert isinstance(target, int)

    if target // 2 > max(nums):
        return []

    hash_table = dict()
    for i, element in enumerate(nums):
        if element in hash_table:
            hash_table[element].append(i)
        else:
            hash_table[element] = [i, ]

    for element in nums:

        if element == target // 2:
            if hash_table.get(element) and len(hash_table[element]) >= 2:
                return hash_table[element][:2]

        elif hash_table.get(target - element):
            return [hash_table.get(element)[0], hash_table.get(target - element)[0]]

def twoSum_better(nums: list, target: int) -> list:
    """
    Return pair from integers from nums wich sum is target
    :param nums: list of integers
    :param target: integer
    :return: list of two integers
    """

    assert isinstance(nums, list)
    assert isinstance(target, int)

    if target // 2 > max(nums):
        return []

    hash_table = dict()
    for i, element in enumerate(nums):
        different = target - element
        if different in hash_table:
            return [i, hash_table[different]]
        else:
            hash_table[element] = i


if __name__ == "__main__":
    test_array = [3, 3]
    test_target = 6
    print(f"we get {test_target} if sum elements of array {twoSum_better(test_array, test_target)}")
