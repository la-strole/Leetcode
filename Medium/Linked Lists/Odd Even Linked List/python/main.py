from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"{self.val}, {self.next()}"


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        odd_pointer = head
        even_pointer = head.next
        first_even = even_pointer

        if not even_pointer:
            return head

        else:
            pointer = even_pointer.next
            odd = True
            while pointer:
                if odd:
                    odd_pointer.next = pointer
                    odd_pointer = odd_pointer.next
                    odd = False
                else:
                    even_pointer.next = pointer
                    even_pointer = even_pointer.next
                    odd = True

                pointer = pointer.next

        even_pointer.next = None
        odd_pointer.next = first_even
        return head


if __name__ == "__main__":
    l1 = [2, 1, 3, 5, 6, 4, 7]

    l1_node = ListNode(val=l1[0])
    l1_start_node = l1_node

    for item in range(1, len(l1)):
        l1_node.next = ListNode(val=l1[item])
        l1_node = l1_node.next

    result = Solution().oddEvenList(l1_start_node)

    while True:
        try:
            print(result.val)
            result = result.next
        except AttributeError:
            break
