class Solution:
    def threeSum(self, nums):

        result = []
        d = {}

        # Hash table
        for value, key in enumerate(nums):
            if key in d.keys():
                d[key].append(value)
            else:
                d[key] = [value]

        # Fix first argument
        for x in range(len(nums) - 2):
            # Fix second argument
            for y in range(x + 1, len(nums)):

                third = -nums[x] - nums[y]
                if third in d:
                    if d[third][-1] > y:
                        answer = sorted([nums[x], nums[y], -nums[x] - nums[y]])
                        if answer not in result:
                            result.append([answer])
        return result

    def threeSum2(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    nums = [0] * 2999
    print(Solution().threeSum2(nums))
