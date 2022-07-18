from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        first = second = float('inf')
        for number in nums:
            if number <= first:
                first = number
            elif number <= second:
                second = number
            else:
                return True
        return False


if __name__ == "__main__":
    nums = [2, 4, -2, -3]
    print(Solution().increasingTriplet(nums))
