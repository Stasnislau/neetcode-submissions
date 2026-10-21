class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        if len(s) < 4:
            return []
        s = list(s)
        def backtrack(i, parts, dots_left):
            if i == len(s) and dots_left == 0:
                res.add(''.join(parts))
                return
                
            for j in range(i, min(i+3, len(s))):
                curr = int("".join(s[i:j+1]))
                if j - i > 0 and (curr == 0 or s[i] == '0'):
                    continue
                left = dots_left
                if curr >= 0 and curr < 256:
                    if (i != 0):
                        parts.append('.')
                        left -= 1
                    parts += s[i:j+1]
                    backtrack(j+1, parts, left)
                    if (i != 0):
                        parts.pop()
                    for _ in range(j+1-i):
                        parts.pop()
        backtrack(0, [], 3)
        return list(res)


