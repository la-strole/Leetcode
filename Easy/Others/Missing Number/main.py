class Solution:
    def missingNumber(self, nums) -> int:
        d = dict.fromkeys(range(len(nums) + 1))

        for item in nums:
            d.pop(item)

        return list(d.keys())[0]


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums))
