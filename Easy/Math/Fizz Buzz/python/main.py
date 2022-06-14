class Solution:
    def fizzBuzz(self, n: int):
        return ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x) for x in
                  range(1, n + 1)]


if __name__ == "__main__":
    n = 15
    print(Solution().fizzBuzz(n))
