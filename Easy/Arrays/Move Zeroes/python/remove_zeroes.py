def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_count = nums.count(0)
    try:
        while True:
            nums.remove(0)
    except ValueError:
        nums.extend([0 for _ in range(zero_count)])


def moveZeroes_better(nums):
    no_zero_position = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[no_zero_position] = nums[i]
            no_zero_position += 1

    while no_zero_position < len(nums):
        nums[no_zero_position] = 0
        no_zero_position += 1


if __name__ == "__main__":
    test_array = [1, 0, 2, 3, 0, 0, 4, 5, 0, 6, 7, 0]
    moveZeroes_better(test_array)
    print(test_array)
