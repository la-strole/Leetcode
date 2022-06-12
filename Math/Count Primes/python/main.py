import math


class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 3:
            return 0

        primes = [1] * n

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i] == 1:
                primes[i * i: n: i] = [0] * len(primes[i * i: n: i])

        return sum(primes) - 2


if __name__ == "__main__":
    n = 10
    print(Solution().countPrimes(n))
