# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:

    @staticmethod
    def isBadVersion(n, array):
        if array[n - 1] == 'w':
            return False
        else:
            return True

    def firstBadVersion(self) -> int:

        black = 4
        n = 5
        assert black <= n

        test_array = []
        for i in range(n):
            if i < black - 1:
                test_array.append('w')
            else:
                test_array.append('b')

        def helper(low, hi):

            if low >= hi:
                if Solution.isBadVersion(low, test_array):
                    return low
                else:
                    return low + 1

            mid = (low + hi) // 2

            if Solution.isBadVersion(mid, test_array):
                hi = mid - 1
            else:
                low = mid + 1

            return helper(low, hi)

        return helper(1, n)

    def better_solution(self, n):
        low, hi = 1, n
        while low < hi:
            mid = low + (hi - low) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    print(f"first black = {Solution().firstBadVersion()}")
