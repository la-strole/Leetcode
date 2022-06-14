class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 1:
            return True

        result = 1
        while result <= n:
            if result == n:
                return True
            result = result * 3
        return False


if __name__ == "__main__":
    n = 9
    print(Solution().isPowerOfThree(n))
