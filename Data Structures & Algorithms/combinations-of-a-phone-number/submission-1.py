class Solution:
    alph = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        alph = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        def backtracking(curr_index, path):
            if curr_index == len(digits):
                ans.append("".join(path))
                return
            curr_options = self.alph[digits[curr_index]]
            for char in curr_options:
                path.append(char)
                backtracking(curr_index+1, path)
                path.pop()
        backtracking(0, [])
        return ans