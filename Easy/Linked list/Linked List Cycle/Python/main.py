# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        fast_ptr =  head
        slow_ptr = head
        try:
            while fast_ptr:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
                if fast_ptr == slow_ptr:
                    return True
        except AttributeError:
            return False
