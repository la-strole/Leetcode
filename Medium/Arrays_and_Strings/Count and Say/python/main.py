from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"

        result = '1'
        while n > 1:
            result = ''.join([f'{len(list(g))}{k}' for k, g in groupby(result)])
            n -= 1
        return result


if __name__ == "__main__":
    n = 4
    print(Solution().countAndSay(n))
