class Solution:
    def maxSubArray_brute_force(self, nums) -> int:
        """
        O(n**2)
        :param nums: Integer array
        :return: max sum
        """
        max_sum = 0
        for start in range(0, len(nums)):
            for end in range(start, len(nums)):
                summary = sum(nums[start:end + 1])
                if summary > max_sum:
                    max_sum = summary
        return max_sum

    def maxSubArray_DP_1(self, nums) -> int:

        # Create array to store local maximum
        local_maximums = [nums[0]]

        for i in range(0, len(nums) - 1):

            if local_maximums[i] > 0:
                local_maximums.append(nums[i + 1] + local_maximums[i])
            else:
                local_maximums.append(nums[i + 1])

        # return global maximum
        return max(local_maximums)

    def maxSubArray_DP_2(self, nums) -> int:

        """
        a - --- b - --- c - --- d, find[b, c] has max sum
        sum([b, c]) = sum([a, c]) - sum([a, b]);
        so within[a, c], we find the b point that has min value of sum([a, b])
        """
        min_sum = 0
        max_sum = float("-Inf")
        temp_sum = 0

        for i in range(0, len(nums)):
            temp_sum += nums[i]
            # local maximum
            max_sum = max(max_sum, temp_sum - min_sum)
            min_sum = min(min_sum, temp_sum)

        return max_sum





if __name__ == '__main__':
    test_array = [[-2, 1, -3, 4, -1, 2, 1, -5, 4],
                  [1],
                  [5, 4, -1, 7, 8]]

    for test_case in test_array:
        print(f"Result is {Solution().maxSubArray_brute_force(test_case)}")

    for test_case in test_array:
        print(f"Result is {Solution().maxSubArray_DP_1(test_case)}")

    for test_case in test_array:
        print(f"Result is {Solution().maxSubArray_DP_2(test_case)}")
