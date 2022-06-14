class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 1

        while all([s.startswith(strs[0][0:index]) for s in strs]) or index <= len(strs[0]):
            index += 1
        return strs[0][0:index - 1]


if __name__ == "__main__":
    strs = ["dog", "racecar", "car"]
    print(Solution().longestCommonPrefix(strs))
