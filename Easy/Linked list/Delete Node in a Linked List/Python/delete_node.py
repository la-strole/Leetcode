# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        victim_node = node.next
        
        node.val = node.next.val
        node.next = node.next.next
        
        del victim_node
        
if __name__ == "__main__":

    # make test linked list
    linked_list = [ListNode(i) for i in range(5)]
    for i in range(len(linked_list) - 1):
        linked_list[i].next = linked_list[i+1]
    

    # try to delete node  = 3
    test_node = 3
    print(f"{[node.val for node in linked_list]}")
    Solution().deleteNode(linked_list[test_node])
    print(f"result {[node.val for node in linked_list]}")