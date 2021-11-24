class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_format = [i.lower() for i in s if i.isalnum()]

        for i in range(len(s_format) // 2):
            if s_format[i] != s_format[-1 - i]:
                return False
        return True


if __name__ == "__main__":
    test_s = "A man, a plan, a canal: Panama"
    print(f"'{test_s}' palindrome? - {Solution().isPalindrome(test_s)}")
