from random import randint


class Solution:
    def removeDuplicates(self, nums: list) -> int:

        point_2 = 0
        for point_1 in range(1, len(nums)):
            if nums[point_1] != nums[point_1 - 1]:
                point_2 += 1
                nums[point_2] = nums[point_1]
        return point_2 + 1


if __name__ == "__main__":
    solution = Solution()
    nums = [randint(-10, 10) for _ in range(20)]
    nums.sort()
    print(solution.removeDuplicates(nums))
    print(nums)
