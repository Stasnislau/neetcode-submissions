class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(left, right, curr_str):
            if left == n and right == n:
                res.append("".join(curr_str))
                return
            if left < right:
                return 
            if left < n:
                curr_str.append('(')
                backtrack(left + 1, right, curr_str)
                curr_str.pop()
            if right < n:
                curr_str.append(')')
                backtrack(left, right + 1, curr_str)
                curr_str.pop()
        backtrack(0,0, [])
        return res
