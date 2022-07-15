from typing import List, Dict, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def word_mask(word: str):
            word_mask = [0] * 26
            for letter in word:
                word_mask[ord(letter) - 97] += 1

            return tuple(word_mask)

        anagrams: Dict[str, List[str]] = {}

        for word in strs:
            mask = word_mask(word)
            if mask in anagrams.keys():
               anagrams[mask].append(word)
            else:
                anagrams[mask] = [word]

        return anagrams.values()


if __name__ == "__main__":
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = ["bdddddddddd", "bbbbbbbbbbc"]
    # strs = [""]
    # strs = ["a"]
    print(Solution().groupAnagrams(strs))
