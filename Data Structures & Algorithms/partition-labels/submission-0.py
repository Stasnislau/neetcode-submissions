class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        res = []
        curr_letters = set()
        last_start = 0
        for i in range(len(s)):
            count[s[i]] -= 1
            curr_letters.add(s[i])
            if count[s[i]] == 0:
                curr_letters.remove(s[i])
                if len(curr_letters) == 0:
                    res.append(i - last_start + 1)
                    last_start = i+1
        return res
            
