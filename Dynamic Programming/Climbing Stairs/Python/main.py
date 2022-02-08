class Solution:

    def climbStairs(self, n: int) -> int:
        array = {1: 1, 2: 2, 3: 3}

        def helper(n, array):
            if n == 1 or n == 2 or n == 3:
                return array[n]

            if n in array:
                return array[n]

            array[n] = helper(n - 2, array) * 2 + helper(n - 3, array)
            return array[n]

        return helper(n, array)

    def climbStairs_2(self, n: int) -> int:
        """
        f(n) = f(n-1) + f(n-2) - fibonachi
        """

        if n <= 3:
            return n

        n1 = 1
        n2 = 2

        for i in range(3, n + 1):
            n1, n2 = n2, n1 + n2

        return n2

if __name__ == "__main__":
    n = 6
    print(f"result is {Solution().climbStairs(n)} steps")
