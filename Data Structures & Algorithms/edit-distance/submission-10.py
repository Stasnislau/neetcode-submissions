class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev_row = [i for i in range(len(word1) + 1)]

        for r in range(1, len(word2) + 1):
            row = [0 for _ in range(len(word1) + 1)]
            for c in range(len(word1) + 1):
                if c == 0:
                    row[c] = r
                    continue
                if word1[c-1] == word2[r-1]:
                    row[c] = prev_row[c-1]
                else:
                    options = [row[c-1], prev_row[c-1], prev_row[c]]
                    row[c] = 1 + min(options)
            prev_row = row

        return prev_row[len(word1)]
