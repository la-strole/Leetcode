# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return self.val

    def __repr__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head, n: int):

        # use dummy head will make the removal of head node easier
        dummy_head = ListNode(-1)
        dummy_head.next = head

        # cur keeps iteration till the end
        # prev_of_removal traverses to the previous node of the one of being removed
        cur, prev_of_removal = dummy_head, dummy_head

        while cur.next != None:

            # n-step delay for prev_of_removal
            if n <= 0:
                prev_of_removal = prev_of_removal.next

            cur = cur.next

            n -= 1

        # Remove the N-th node from end of list
        n_th_node = prev_of_removal.next
        prev_of_removal.next = n_th_node.next

        del n_th_node

        return dummy_head.next


