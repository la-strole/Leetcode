class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        stack = []
        for letter in s:
            if letter in d:
                if not stack or stack.pop() != d[letter]:
                    return False

            else:
                stack.append(letter)
        if not stack:
            return True
        return False


if __name__ == "__main__":
    s = "(]"
    print(Solution().isValid(s))
