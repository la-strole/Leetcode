class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        if len(nums) <= 2:
            return max(nums[0], nums[1])

        memo_dict = {}

        def helper(index):

            if index in memo_dict:
                return memo_dict[index]

            if index > len(nums) - 1:
                return 0

            memo_dict[index] = nums[index] + max(helper(index + 2), helper(index + 3))
            return memo_dict[index]

        return max(helper(0), helper(1))

    def rob2(self, nums) -> int:
        maxList = [0] * len(nums)

        for i in range(len(maxList)):
            maxList[i] = nums[i]
            if i >= 3:
                maxList[i] += max(maxList[i - 2], maxList[i - 3])
            elif i == 2:
                maxList[i] += maxList[i - 2]

        return max(maxList)


if __name__ == '__main__':
    test_nums = [2, 7, 9, 3, 1]
    print(f"Result is {Solution().rob(test_nums)}")
    print(f"Result is {Solution().rob2(test_nums)}")


