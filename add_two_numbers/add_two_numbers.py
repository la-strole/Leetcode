# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def __repr__(self):
         return str(self.val)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):

        node1 = l1
        node2 = l2
        empt = ListNode(val=0, next=None)

        prev = 0

        result = list()

        while not result or node1 or node2 or prev == 1:

            if node1:
                s1 = node1.val
                node1 = node1.next
            else:
                s1 = 0

            if node2:
                s2 = node2.val
                node2 = node2.next
            else:
                s2 = 0

            s = (s1 + s2 + prev)
            result.append(ListNode(val=s % 10))
            if s >= 10:
                prev = 1
            else:
                prev = 0




        for number in range(len(result) - 1):
            result[number].next = result[number + 1]


        return result




if __name__ == '__main__':

    l1 = [3, 5]
    l2 = [4]

    list_array1 = [ListNode(val=i) for i in l1]
    for number in range(len(list_array1) - 1):
        list_array1[number].next = list_array1[number + 1]

    list_array2 = [ListNode(val=i) for i in l2]
    for number in range(len(list_array2) - 1):
        list_array2[number].next = list_array2[number + 1]

    result = Solution()
    print(result.addTwoNumbers(list_array1[0], list_array2[0]))
