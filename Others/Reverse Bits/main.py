class Solution:
    def reverseBits(self, n: int) -> int:
        rever = bin(n)[-1:1:-1]
        rever = rever.ljust(32, '0')
        return int(rever, 2)


if __name__ == "__main__":
    n = 43261596
    print(Solution().reverseBits(n))
