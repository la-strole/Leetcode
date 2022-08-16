from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=None):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Find length of lists and if they are intersect (if there last nod is equal.)
        l1, l2 = 0, 0
        p1, p2 = headA, headB
        while p1 and p2:
            l1 += 1
            p1 = p1.next
            l2 += 1
            p2 = p2.next
        if p1:
            while p1:
                l1 += 1
                p1 = p1.next
        elif p2:
            while p2:
                l2 += 1
                p2 = p2.next

        if p1 != p2:
            return None

        # Find first intersection node.
        if l1 > l2:
            for _ in range(l1 - l2):
                headA = headA.next
        elif l2 > l1:
            for _ in range(l2 - l1):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def getIntersectionNode2(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None
    
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