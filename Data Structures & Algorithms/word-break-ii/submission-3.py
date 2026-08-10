import string
class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Node()
        res = []
        def add_word(word):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.is_end = True
        path = []
        for word in wordDict:
            add_word(word)
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(path))
                return
            curr = root
            for j in range(i, len(s)):
                if s[j] in curr.children:
                    curr = curr.children[s[j]]
                else:
                    return
                if curr.is_end:
                    path.append(s[i:j+1])
                    backtrack(j+1)
                    path.pop()
        backtrack(0)
        return res
