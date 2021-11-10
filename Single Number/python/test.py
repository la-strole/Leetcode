import single_number
import unittest
from timeit import timeit
from random import randint

class TestSingleNumber(unittest.TestCase):
    @staticmethod
    def create_test_array():
        """
        return test array where only one random element is non duplicate.
        :return: (list of integers, single element)
        """
        nums = []
        for _ in range(randint(1, 3 * pow(10, 4) + 1) // 2):
            nums.append(_)
            nums.append(_)
        element = nums.pop(randint(0, len(nums)))
        return nums, element

    def test_single_number_
    def test_single_number_right_answer(self):
        for
