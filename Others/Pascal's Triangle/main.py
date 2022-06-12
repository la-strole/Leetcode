class Solution:
    def generate(self, numRows: int):

        result = [[1], [1, 1], [1, 2, 1]]
        if numRows <= 3:
            return result[:numRows]

        while len(result) < numRows:
            index = 1
            row = [1]
            while index < len(result[-1]):
                row.append(result[-1][index - 1] + result[-1][index])
                index += 1
            row.append(1)
            result.append(row)

        return result


if __name__ == "__main__":
    n = 2
    print(Solution().generate(n))
