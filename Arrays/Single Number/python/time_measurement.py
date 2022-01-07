import single_number
from timeit import timeit
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


def time_measurement():
    print(
        f"single_number    time: {timeit('single_number.singleNumber(create_test_array()[0])', globals=globals(), number=1000)}")
    print(
        f"single_number_v2 time: {timeit('single_number.singleNumber_v2(create_test_array()[0])', globals=globals(), number=1000)}"
    )


if __name__ == '__main__':
    time_measurement()
