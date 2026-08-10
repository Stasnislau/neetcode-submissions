class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtracking(start_index, curr_strs):
            if start_index == len(s):
                res.append(curr_strs.copy())
            
            for i in range (start_index, len(s)):
                curr_str = s[start_index: i+1]
                if curr_str[::-1] == curr_str:
                    curr_strs.append(curr_str)
                    backtracking(i+1, curr_strs)
                    curr_strs.pop()
            

        backtracking(0, [])
        return res