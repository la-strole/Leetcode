class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Create pointers to max elements from arrays
        left_array_point = m - 1
        right_array_point = n - 1
        current_point = m + n - 1

        # Iterate through helper array
        while left_array_point >= 0 and right_array_point >= 0:

            if nums1[left_array_point] >= nums2[right_array_point]:
                nums1[current_point] = nums1[left_array_point]
                left_array_point -= 1
            else:
                nums1[current_point] = nums2[right_array_point]
                right_array_point -= 1

            current_point -= 1

        # If there are right remainder
        if right_array_point >= 0:
            for i in range(right_array_point + 1):
                nums1[i] = nums2[i]


if __name__ == "__main__":
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3


    Solution().merge(nums1, m, nums2, n)

    print(f"Result is {nums1}")
