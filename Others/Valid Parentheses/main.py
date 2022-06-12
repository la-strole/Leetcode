class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '[': ']', '{':'}'}
        close_index = 0
        close_flag = 0
        for letter in s:
            if close_flag == 0 and letter not in d.values():
                return False
            elif letter in d.keys():
                close_flag = 1
                while close_index >= 0:
                    if s[close_index - 1] != d[s[close_index]]:
                        return False


            close_index += 1



if __name__ == "__main__":
    s =