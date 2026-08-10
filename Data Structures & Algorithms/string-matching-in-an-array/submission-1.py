class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        mapping = set(words)
        res = set()
        for word in words:
            for i in range(len(word) -1):
                for j in range(i, len(word)):
                    curr = word[i:j+1]
                    if curr == word:
                        continue
                    if curr in mapping:
                        res.add(curr)
        return list(res)