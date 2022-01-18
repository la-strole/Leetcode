# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        max_depth = 0
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1

        def inOrderTraversal(node, depth):
            if not node:
                return depth
            return max(inOrderTraversal(node.left, depth + 1), inOrderTraversal(node.right, depth + 1))

        return inOrderTraversal(root, max_depth)

    def betterSolution(self, root):

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)


    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.val)
            self.inOrder(node.right)


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    def makeTreeFromList(array):
        """
        Makes binary tree from list - tree has to be perfect - there for add None nodes - later they are deleted
        :param array: list if nodes values in order parent, leftChild, rightChild, leftGrandSon, rightGrandSon etc
        :return: array of Node instances with left, right children -  root is result[0]
        """

        if not array:
            return [None, ]
        if len(array) == 1:
            return [TreeNode(array[0]), ]

        test_tree = list(map(TreeNode, array))

        depth = math.log2(len(test_tree) + 1)

        index = 0

        for i in range(int(depth)):
            index2 = 0
            try:
                while index < (2 ** (i + 1)) - 1:
                    test_tree[index].left = test_tree[2 ** (i + 1) - 1 + index2]
                    index2 += 1
                    test_tree[index].right = test_tree[2 ** (i + 1) - 1 + index2]
                    index2 += 1
                    index += 1
            except IndexError:
                continue
        # Delete None nodes - replace them with None values for parent
        for node in test_tree:
            if node.left and node.left.val == None:
                node.left = None
            if node.right and node.right.val == None:
                node.right = None

        return test_tree


    test_list = ([3, 9, 20, None, None, 15, 7],
                 [],
                 [1])

    for test_case in test_list:
        print(f"max depth is {Solution().maxDepth(makeTreeFromList(test_case)[0])}")

    for test_case in test_list:
        print(f"max depth is {Solution().betterSolution(makeTreeFromList(test_case)[0])}")