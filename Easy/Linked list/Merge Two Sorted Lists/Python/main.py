# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        if not list1:
            return list2

        if not list2:
            return list1

        l1_head = list1
        l2_head = list2

        if list1.val < list2.val:
            result_head = list1
            l1_head = list1.next
        else:
            result_head = list2
            l2_head = list2.next

        result_node = result_head

        while l1_head and l2_head:
            if l1_head.val < l2_head.val:
                result_node.next = l1_head
                l1_head = l1_head.next
                result_node = result_node.next
            else:
                result_node.next = l2_head
                l2_head = l2_head.next
                result_node = result_node.next
        if l1_head:
            result_node.next = l1_head
        elif l2_head:
            result_node.next = l2_head

        return result_head

    def mergeTwoLists_v2(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2

        return dummy.next


if __name__ == "__main__":
    list1 = list(map(ListNode, [1, 2, 4]))
    list2 = list(map(ListNode, [1, 3, 4]))
    for i in range(len(list1) - 1):
        list1[i].next = list1[i + 1]
    for i in range(len(list2) - 1):
        list2[i].next = list2[i + 1]

    result_head = Solution().mergeTwoLists(list1[0], list2[0])

    answer = []
    while result_head:
        answer.append(result_head.val)
        result_head = result_head.next

    print(answer)
