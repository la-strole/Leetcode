import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]].append(i)
            else:
                d[s[i]] = [i, ]

        unique = [d[i] for i in d.keys() if len(d[i]) == 1]
        if unique:
            return min(unique)[0]
        return -1

    def firstUniqChar_v2(self, s: str) -> int:

        d = collections.Counter(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    test_s = "loveleetcode"
    print(f"first index of unique element in '{test_s}' is {Solution.firstUniqChar(Solution(), test_s)}")
    print(f"first index of unique element in '{test_s}' is {Solution.firstUniqChar_v2(Solution(), test_s)}")