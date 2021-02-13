# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def __repr__(self):
         return str(self.val)

class Solution:
    def addTwoNumbers(self, l1, l2):

        def get_node_value(l, number):
            try:
                return l[number].val
            except IndexError:
                return 0

        max_len = max(len(l1), len(l2))

        result = [ListNode() for _ in range(max_len + 1)]
        for number in range(max_len):
            result[number].next = result[number + 1]

        for num, node in enumerate(result):

            s = get_node_value(l1, num) + get_node_value(l2, num)
            if s + node.val < 10:
                node.val += s
            else:
                node.val = (node.val + s) % 10
                node.next.val += 1

        if result[-1].val == 0:
            result.pop()

        return result




if __name__ == '__main__':
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    list_array1 = [ListNode(val=i) for i in l1]
    for number in range(len(list_array1) - 1):
        list_array1[number].next = list_array1[number + 1]

    list_array2 = [ListNode(val=i) for i in l2]
    for number in range(len(list_array2) - 1):
        list_array2[number].next = list_array2[number + 1]

    result = Solution()
    print(result.addTwoNumbers(list_array1, list_array2))
