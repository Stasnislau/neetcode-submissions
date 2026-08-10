from functools import cache
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr_arr = [1] * k
        def backtrack(i, j):
            for num in range(i, n + 1 - (k - j - 1)):
                curr_arr[j] = num
                if j == k - 1:
                    res.append(curr_arr.copy())
                else:
                    backtrack(num+1, j + 1)
        backtrack(1, 0)
        return res