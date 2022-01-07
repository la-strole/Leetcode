from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    test_s = "anagram"
    test_t = "car"
    print(f"is '{test_t}' and '{test_s}' anagrams? - {Solution().isAnagram(test_s, test_t)}")
