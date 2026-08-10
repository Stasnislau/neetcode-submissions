class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        for i in range(1, len(words)):
            j = 0
            min_len = min(len(words[i-1]), len(words[i]))
            while j < min_len:
                c1 = words[i-1][j]
                c2 = words[i][j]
                if dic[c1] != dic[c2]:
                    if dic[c1] > dic[c2]:
                        return False
                    else:
                        break
                j += 1
            if j == min_len and j < len(words[i-1]):
                return False
        return True