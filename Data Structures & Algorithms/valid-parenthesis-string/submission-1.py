class Solution:
    def checkValidString(self, s: str) -> bool:
        c_min = 0
        c_max = 0
        for i in range(len(s)):
            
            if s[i] == '(':
                c_min += 1
                c_max += 1
            elif s[i] == ')':
                c_min -= 1
                c_max -= 1
            else:
                c_min -= 1
                c_max += 1
            if c_max < 0:
                return False
            c_min = max(c_min, 0)
        return c_min == 0