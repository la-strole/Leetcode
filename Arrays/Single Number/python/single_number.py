from random import randint
from timeit import timeit


def singleNumber(nums: list) -> int:
    """
    return non-duplicate element
    :param nums: list of integers
    :return: non duplicate integer
    """

    assert isinstance(nums, list)
    assert 1 <= len(nums) <= 3 * pow(10, 4)
    assert len(nums) % 2 == 1
    for _ in nums:
        assert isinstance(_, int)
        assert -3 * pow(10, 4) <= _ <= 3 * pow(10, 4)

    # sort array
    nums.sort()
    # look for non-duplicates
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]


def singleNumber_v2(nums) -> int:

    assert isinstance(nums, list)
    assert 1 <= len(nums) <= 3 * pow(10, 4)
    assert len(nums) % 2 == 1
    for _ in nums:
        assert isinstance(_, int)
        assert -3 * pow(10, 4) <= _ <= 3 * pow(10, 4)
    res = 0
    for i in nums:
        res = res ^ i
    return res


if __name__ == "__main__":
    test_array = [4, 1, 2, 1, 2]
    print(f"non duplicate element is {singleNumber(test_array)}")
