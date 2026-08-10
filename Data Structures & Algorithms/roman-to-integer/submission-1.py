class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        if len(s) == 1:
            return values[s]
        i = 1
        while i < len(s):
            if values[s[i-1]] < values[s[i]]:
                res += values[s[i-1:i+1]]
                i += 1
            else:
                res += values[s[i-1]]   
                if i == len(s) - 1:
                    res += values[s[i]]  
            i += 1         
        return res