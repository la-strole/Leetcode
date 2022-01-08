class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        palindrome = []
        while head:
            palindrome.append(head.val)
            head = head.next
        for i in range(len(palindrome) // 2):
            if palindrome[i] != palindrome[-1-i]:
                return False
        return True


if __name__ == "__main__":
    test_list = list(map(ListNode, [1]))
    for i in range(len(test_list) - 1):
        test_list[i].next = test_list[i + 1]

    print(Solution().isPalindrome(test_list[0]))
