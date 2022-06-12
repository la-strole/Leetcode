from collections import OrderedDict
class Solution:
    def romanToInt(self, s: str) -> int:

        alphabet = OrderedDict({
                    'IV': 4,
                    'IX': 9,
                    'XL': 40,
                    'XC': 90,
                    'CD': 400,
                    'CM': 900,
                    'X': 10,
                    'V': 5,
                    'I': 1,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
        })
        result = 0
        while s:
            for key in alphabet:
                if s.startswith(key):
                    result += alphabet[key]
                    s = s[len(key):]
                    break
        return result


if __name__ == "__main__":
    s = "MCDLXXVI"
    print(Solution().romanToInt(s))
