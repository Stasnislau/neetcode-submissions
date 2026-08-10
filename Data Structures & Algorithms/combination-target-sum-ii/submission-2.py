class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(j, curr_nums, curr_sum):
                
                if curr_sum == target:
                    res.append(curr_nums.copy())
                    return
                if j == len(candidates) or curr_sum > target:
                    return
                curr_nums.append(candidates[j])
                dfs(j+1, curr_nums, curr_sum + candidates[j])
                curr_nums.pop()
                i = j
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                dfs(i + 1, curr_nums, curr_sum)
                
                    


        dfs(0, [], 0)
        return res