# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

    def __repr__(self):
        return str(self.val)


class Solution:

    def levelOrder(self, root):
        if root:
            order_list = [[root.val]]
            parent_list = [root]

            while parent_list:
                child_list = []

                for node in parent_list:
                    if node and (node.left or node.right):
                        if node.left:
                            child_list.append(node.left)
                        if node.right:
                            child_list.append(node.right)

                if child_list:
                    order_list.append([item.val for item in child_list])

                parent_list = child_list[:]

            return order_list

        else:
            return []

    def levelOrderBetter(self, root):

        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans

if __name__ == "__main__":

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


    test_list = ([1, 2, 3, 4, None, None, 5],
                 [1, 1],
                 [2, 2, 2],
                 [2, 1, 3],
                 [3, 9, 20, None, None, 15, 7],
                 [],
                 [1]
                 )

    for test_case in test_list:
        print(f"Level order {Solution().levelOrderBetter(makeTreeFromList(test_case)[0])}")
