class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result_pointer = ListNode(val=(l1.val + l2.val) % 10)
        result_start_pointer = result_pointer
        exceed = 0
        if l1.val + l2.val >= 10:
            exceed = 1
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            if l1 and l2:
                add_value = l1.val + l2.val + exceed
                l1 = l1.next
                l2 = l2.next
            elif l1:
                add_value = l1.val + exceed
                l1 = l1.next
            elif l2:
                add_value = l2.val + exceed
                l2 = l2.next
            else:
                raise ValueError
            result_pointer.next = ListNode(val=add_value % 10)
            if add_value >= 10:
                exceed = 1
            else:
                exceed = 0
            result_pointer = result_pointer.next

        if exceed == 1:
            result_pointer.next = ListNode(val=1)

        return result_start_pointer


if __name__ == "__main__":
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]

    l1_node = ListNode(val=l1[0])
    l1_start_node = l1_node
    l2_node = ListNode(val=l2[0])
    l2_start_node = l2_node

    for item in range(1, len(l1)):
        l1_node.next = ListNode(val=l1[item])
        l1_node = l1_node.next

    for item in range(1, len(l2)):
        l2_node.next = ListNode(val=l2[item])
        l2_node = l2_node.next

    result = Solution().addTwoNumbers(l1_start_node, l2_start_node)

    while True:
        try:
            print(result.val)
            result = result.next
        except AttributeError:
            break
