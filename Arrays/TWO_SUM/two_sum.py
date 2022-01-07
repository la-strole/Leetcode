class Solution:
    def twoSum(self, nums, target) -> list:

        for first_number in range(len(nums)):
            for second_number in range(first_number + 1, len(nums)):
                if nums[first_number] + nums[second_number] == target:
                    return [first_number, second_number]

    def best(self, nums, target) -> list:

        d = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in d:
                d[num] = i
            else:
                return [d[n], i]


task = Solution()
print(task.twoSum([3,2,4], 6))
print(task.best([3,2,4], 6))