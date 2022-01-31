# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        
        def helper(lo, hi):
            # Base case
            if lo > hi:
                return None

            mid = (lo + hi) // 2

            node = TreeNode(val=nums[mid])
            node.left = helper(lo=lo, hi=mid - 1)
            node.right = helper(lo=mid + 1, hi=hi)

            return node

        return helper(0, len(nums) - 1)
