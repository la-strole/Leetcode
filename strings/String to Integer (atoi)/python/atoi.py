class Solution:

    def myAtoi(self, s: str) -> int:

        positive = 1
        result = 0
        i = 0

        if len(s) == 0:
            return 0

        while s[i] == " " and i < len(s) - 1:
            i += 1
        if s[i] == '+':
            i += 1
        elif s[i] == "-":
            positive = -1
            i += 1
        elif not s[i].isdigit():
            return 0
        index = i
        while i < len(s) and s[i].isdigit():
            # 9 digits without check overload
            if i < index + 9:
                result = result * 10 + ord(s[i]) - ord('0')
                i += 1
                continue
            # else: check overload once
            if positive == 1:
                if result > 214748364 or (result == 214748364 and ord(s[i]) - ord('0') > (pow(2, 31) - 1) % 10):
                    return pow(2, 31) - 1
                else:
                    result = result * 10 + ord(s[i]) - ord('0')
                    i += 1
                    continue
            else:
                if result > 214748364 or (result == 214748364 and ord(s[i]) - ord('0') > pow(2, 31)  % 10):
                    return -1 * pow(2, 31)
                else:
                    result = result * 10 + ord(s[i]) - ord('0')
                    i += 1
                    continue
        return positive * result

    def myAtoi_v2(self, s: str) -> int:
        import re

        positive = 1
        mask = re.compile(r"^ *([\+-]?)0*(\d+)")
        digital_string = re.match(mask, s)
        if not digital_string:
            return 0
        if len(digital_string.groups()) > 1:
            if digital_string.groups()[0] == "-":
                positive = -1

        digitals = digital_string.groups()[-1]

        if len(digitals) <= 9:
            return int(digitals) * positive
        elif len(digitals) == 10:
            if positive == 1:
                if digitals < str(pow(2, 31) - 1):
                    return int(digitals)
                else:
                    return pow(2, 31) - 1
            else:
                if digitals < str(pow(2, 31)):
                    return int(digitals) * positive
                else:
                    return -1 * pow(2, 31)
        else:
            if positive == -1:
                return -1 * pow(2, 31)
            return pow(2, 31) - 1


if __name__ == "__main__":

    tests = ("21474836460", "", "42", "-42", "+42", "  -42", "+-42", " +-42", "42somewords", "2147483648", "2147483647",
             "-2147483648", "21474836480", "-214748364862", " ", "  0000000000012345678", "   -115579378e25")
    for test in tests:
        print(f"number from {test} is {Solution().myAtoi_v2(test)}")
