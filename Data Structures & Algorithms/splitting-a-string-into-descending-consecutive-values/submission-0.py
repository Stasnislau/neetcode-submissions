class Solution:
    def splitString(self, s: str) -> bool:
        dp  = {}
        def backtrack(i, prev = None):
            if (i, prev) in dp:
                return dp[(i, prev)]
            if i == len(s):
                dp[(i, prev)] = True
                if prev is None:
                    dp[(i, prev)] = False
                return dp[(i, prev)]
            curr_res = False
            curr = 0
            end = len(s) - 1 if prev is None else len(s)
            for j in range(i, end):
                curr = int(s[i:j+1])
                if prev is None or (prev is not None and curr == prev - 1):
                    curr_res = curr_res or backtrack(j+1, curr) 
            dp[(i, prev)] = curr_res
            return dp[(i, prev)]
        res = backtrack(0)
        print(dp)
        return res