class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = min(len(str1), len(str2))
        if len(str1) < len(str2):
            str2, str1 = str1, str2
        for i in range(min_len, 0, -1):
            if len(str1) % i != 0 or len(str2) % i != 0:
                continue
            print(i)
            t1 = len(str1) // i
            t2 = len(str2) // i
            print(str1[:i] * t1 == str1, str1[:i] * t1,t1, str1)
            if str1[:i] * t1 == str1 and str1[:i] * t2 == str2:
                return str1[:i]
        return ''