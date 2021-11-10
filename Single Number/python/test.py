import single_number
import unittest
from random import randint


def create_test_array():
    """
    return test array where only one random element is non duplicate.
    :return: (list of integers, single element)
    """
    nums = []
    for _ in range(randint(1, 3 * pow(10, 4) + 1) // 2):
        element = randint(-3 * pow(10, 4), 3 * pow(10, 4))
        nums.append(element)
        nums.append(element)

    answer = nums.pop(randint(0, len(nums) - 1))
    return nums, answer


class TestSingleNumber(unittest.TestCase):

    def test_single_number_border_conditions(self):

        # 1 element
        test_array = [1]
        self.assertEqual(1, single_number.singleNumber(test_array))
        self.assertEqual(1, single_number.singleNumber_v2(test_array))
        # smallest element
        test_array = [-3 * pow(10, 4), 1, 1, 2, 2]
        self.assertEqual(-3 * pow(10, 4), single_number.singleNumber(test_array))
        self.assertEqual(-3 * pow(10, 4), single_number.singleNumber_v2(test_array))
        # biggest element
        test_array = [3 * pow(10, 4), 1, 1, 2, 2]
        self.assertEqual(3 * pow(10, 4), single_number.singleNumber(test_array))
        self.assertEqual(3 * pow(10, 4), single_number.singleNumber_v2(test_array))
        # longest array
        test_array = [1 for _ in range(3 * pow(10, 4) - 2)]
        test_array.append(2)
        self.assertEqual(2, single_number.singleNumber(test_array))
        self.assertEqual(2, single_number.singleNumber_v2(test_array))

    def test_single_number_right_answer(self):
        # random test
        for _ in range(1000):
            test_array, answer = create_test_array()
            if len(test_array) % 2 == 0:
                self.assertRaises(AssertionError, single_number.singleNumber, test_array)
                self.assertRaises(AssertionError, single_number.singleNumber_v2, test_array)
            else:
                self.assertEqual(answer, single_number.singleNumber(test_array))
                self.assertEqual(answer, single_number.singleNumber_v2(test_array))

    def test_single_number_errors(self):
        # wrong type of array (not list)
        test_array = 'string line'
        self.assertRaises(AssertionError, single_number.singleNumber, test_array)
        self.assertRaises(AssertionError, single_number.singleNumber_v2, test_array)
        # wrong array len
        test_array = []
        self.assertRaises(AssertionError, single_number.singleNumber, test_array)
        self.assertRaises(AssertionError, single_number.singleNumber_v2, test_array)
        test_array = [0 for _ in range(3 * pow(10, 4) + 1)]
        self.assertRaises(AssertionError, single_number.singleNumber, test_array)
        self.assertRaises(AssertionError, single_number.singleNumber_v2, test_array)
        # not only integer in array
        test_array = [1, 1, 1, 1, 2, 2, 'r']
        self.assertRaises(AssertionError, single_number.singleNumber, test_array)
        self.assertRaises(AssertionError, single_number.singleNumber_v2, test_array)
        # len of elements is even number
        test_array = [1, 1, 1, 4]
        self.assertRaises(AssertionError, single_number.singleNumber, test_array)
        self.assertRaises(AssertionError, single_number.singleNumber_v2, test_array)
        # We assert that there are not cases than
        # there are more than one non-duplicate elements
        # there are not non-duplicate elements


if __name__ == '__main__':
    unittest.main()

