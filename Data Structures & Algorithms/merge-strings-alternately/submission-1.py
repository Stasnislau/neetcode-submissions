class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        is_reverse = False
        if len(word1) < len(word2):
            word1,word2 = word2,word1
            is_reverse = True
        res = []
        
        for c1, c2 in zip(word1, word2):
            if is_reverse:
                res.append(c2)
            res.append(c1)
            if not is_reverse:
                res.append(c2)
            
        for i in range(len(word2), len(word1)):
            res.append(word1[i])
        return "".join(res)