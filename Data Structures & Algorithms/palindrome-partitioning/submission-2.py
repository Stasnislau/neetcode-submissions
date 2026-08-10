class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtracking(start_index, curr_strs):

            if start_index == len(s):
                res.append(curr_strs.copy())
                return 
                        
            for i in range (start_index, len(s)):
                substring = s[start_index: i + 1]
                if substring[::-1] == substring:
                    curr_strs.append(substring)
                    backtracking(i+1, curr_strs)
                    curr_strs.pop()

        backtracking(0, [])
        return res