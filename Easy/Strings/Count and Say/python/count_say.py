class Solution:
    def countAndSay(self, n: int) -> str:
        def say(value, n):
            alphabet = ""
            unique = value[0]
            count = 0
            for i in range(len(value)):
                if value[i] == unique:
                    count += 1
                else:
                    alphabet = alphabet + str(count) + unique
                    unique = value[i]
                    count = 1
            alphabet = alphabet + str(count) + unique
            if n == 0:
                return alphabet
            else:
                return say(alphabet, n - 1)

        if n == 1:
            return '1'
        else:
            return say("1", n - 2)


if __name__ == "__main__":
    test_n = 30
    #print(f"result of {test_n} is {Solution().countAndSay(test_n)}")
    print(f"length max = {len(Solution().countAndSay(test_n))}")
