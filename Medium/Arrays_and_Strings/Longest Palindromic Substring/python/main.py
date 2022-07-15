from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_palindrom: List[str] = [s[0]]

        for center in range(len(s) - 1):

            if len(max_palindrom) > (len(s) - center) * 2:
                break

            right = center + 1
            temp_palindrom: List[str] = [s[center]]
            while right < len(s) and s[right - 1] == s[right]:
                temp_palindrom.append(s[right])
                right += 1

            left = center -1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                temp_palindrom.append(s[right])
                temp_palindrom.insert(0, s[left])
                left -= 1
                right += 1

            if len(temp_palindrom) > len(max_palindrom):
                max_palindrom = temp_palindrom.copy()

        return ''.join(max_palindrom)


if __name__ == "__main__":
    s = "ababababa"
    # s = "cbbd"
    print(Solution().longestPalindrome(s))
