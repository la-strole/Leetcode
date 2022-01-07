
from timeit import timeit
from random import randint

class Solution:
    def reverse(self, x: int) -> int:
        answer = str(abs(x))[::-1]
        if len(answer) == 10:
            if x > 0 and answer > '2147483647':
                return 0
            if x < 0 and answer > '2147483648':
                return 0

        if x >= 0:
            return int(str(abs(x))[::-1])
        return -int(str(abs(x))[::-1])

    def reverse_v2(self, x: int) -> int:
        reverse_integer = 0;
        max_int = pow(2, 31) - 1
        min_int = -pow(2, 31)
        while x != 0:
            last_digit = x % 10
            x //= 10
            # 7 = 2^31 // 10; 8 = -2^31 // 10
            if reverse_integer > max_int // 10 or (reverse_integer == max_int and last_digit > 7):
                return 0
            if reverse_integer < min_int // 10 or (reverse_integer == min_int and last_digit < -8):
                return 0

            reverse_integer = reverse_integer * 10 + last_digit
        return reverse_integer


if __name__ == "__main__":
    # test_x = randint(-pow(2, 31), pow(2, 31) - 1)
    test_x = 1675305199
    solution = Solution()
    print(f"number is {test_x}, reversed is {solution.reverse(test_x)}")
    print(f"number is {test_x}, reversed is {solution.reverse_v2(test_x)}")

    print(f"time_v1={timeit('solution.reverse(test_x)', globals=globals(), number=1000000)}")
    print(f"time_v2={timeit('solution.reverse_v2(test_x)', globals=globals(), number=1000000)}")