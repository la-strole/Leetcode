class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # constraints
        assert isinstance(nums, list)
        assert 1 <= len(nums) <= pow(10, 5)
        for i in nums:
            assert isinstance(i, int)
            assert -pow(2, 31) <= nums[i] <= pow(2, 31) - 1
        assert isinstance(k, int)
        assert 0 <= k <= pow(10, 5)

        if len(nums):
            shift = k % len(nums)
            if shift:
                nums[:shift], nums[shift:] = nums[-shift:], nums[:-shift]



