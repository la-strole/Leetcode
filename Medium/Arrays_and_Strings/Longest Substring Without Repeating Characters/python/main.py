from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        existed_letters: Dict[str, int] = {}
        left, right = (0, 0)
        longest = 0

        while right < len(s):
            if s[right] in existed_letters.keys():
                if longest < right - left:
                    longest = right - left

                # left is next after first inclusion s[right] in string—it is value in the dict.
                # Delete letters from the dict since we change left.
                for item in range(left, existed_letters[s[right]]):
                    existed_letters.pop(s[item])
                    left += 1
                # Now first inclusion of letter s[right] is right
                existed_letters[s[right]] = right
                left += 1
                right += 1
            else:
                existed_letters[s[right]] = right
                right += 1
        if longest < right - left:
            longest = right - left

        return longest


if __name__ == "__main__":
    s = "abcdefaghijk"
    # s = "bbbbb"
    # s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))
