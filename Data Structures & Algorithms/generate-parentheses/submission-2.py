class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(left,right, curr_arr):
            if left == n and right == n:
                res.append("".join(curr_arr))
            if left > right:
                curr_arr.append(')')
                backtrack(left, right + 1, curr_arr)
                curr_arr.pop()
            if left < n:
                curr_arr.append('(')
                backtrack(left+1, right, curr_arr)
                curr_arr.pop()

            
        backtrack(0,0,[])
        return res
