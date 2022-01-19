# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        value = -2 ** 31 - 1
        valid = True

        def treeTraverse(node):

            nonlocal value
            nonlocal valid

            if node:

                if not valid:
                    return

                treeTraverse(node.left)
                if node.val <= value:
                    valid = False
                    return
                value = node.val
                treeTraverse(node.right)

        treeTraverse(root)
        return valid

    def better_solution(self, node, lo=float(float('-inf')), hi=float('inf')):

        if node:

            if node.val <= lo or node.val >= hi:
                return False

            return self.better_solution(node.left, lo, node.val) and \
                   self.better_solution(node.right, node.val, hi)

        return True


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


    test_list = ([1, 1],
                 [2, 2, 2],
                 [2, 1, 3],
                 [3, 9, 20, None, None, 15, 7],
                 [],
                 [1])

    for test_case in test_list:
        print(f"Valid BST {Solution().isValidBST(makeTreeFromList(test_case)[0])}")

    print("\n")

    for test_case in test_list:
        print(f"Valid BST {Solution().better_solution(makeTreeFromList(test_case)[0])}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
