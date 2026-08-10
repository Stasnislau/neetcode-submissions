class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(j, curr_nums, curr_sum):
                if j == len(candidates) or curr_sum > target:
                    return
                for i in range(j, len(candidates)):
                    if curr_sum + candidates[i] == target:
                        curr_nums.append(candidates[i])
                        res.append(curr_nums.copy())
                        curr_nums.pop()
                        break
                    if i > j and candidates[i] == candidates[i - 1]:
                        continue
                    if curr_sum + candidates[i] > target:
                        break
                    
                    curr_nums.append(candidates[i])
                    dfs(i+1, curr_nums, curr_sum + candidates[i])
                    curr_nums.pop()


        dfs(0, [], 0)
        return res