import pytest
from main import Solution


def test_nums():
    nums = [2, 1, 5, 0, 4, 6]
    assert Solution().increasingTriplet(nums) is True
    nums = [20, 100, 10, 12, 5, 13]
    assert Solution().increasingTriplet(nums) is True
    nums = [5, 4, 3, 2, 1]
    assert Solution().increasingTriplet(nums) is False
    nums = [1, 5, 0, 4, 1, 3]
    assert Solution().increasingTriplet(nums) is True
    nums = [2, 4, -2, -3]
    assert Solution().increasingTriplet(nums) is False
    nums = [1, 2, 3, 4, 5]
    assert Solution().increasingTriplet(nums) is True
