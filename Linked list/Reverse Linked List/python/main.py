# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head):

        if not head:
            return None

        if not head.next:
            return head

        if not head.next.next:
            new_head = head.next
            new_head.next = head
            head.next = None
            return new_head

        ptr0 = head
        ptr1 = head.next
        ptr2 = head.next.next
        head.next = None

        while ptr2:
            ptr1.next = ptr0
            ptr0 = ptr1
            ptr1 = ptr2
            ptr2 = ptr2.next

        ptr1.next = ptr0
        return ptr1


if __name__ == "__main__":
    list_node = [ListNode(i) for i in range(3)]
    for i in range(len(list_node) - 1):
        list_node[i].next = list_node[i + 1]

    answer = []
    node = list_node[0]
    while node:
        answer.append(node)
        node = node.next

    print(answer)

    answer = []
    node = Solution().reverseList(list_node[0])
    while node:
        answer.append(node)
        node = node.next
    print(answer)