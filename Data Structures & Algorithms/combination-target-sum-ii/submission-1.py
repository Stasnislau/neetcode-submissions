class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def dfs(j, curr_nums, rem_trg):
            if j > len(candidates):
                return
            for i in range(j, len(candidates)):
                if i > j and candidates[i - 1] == candidates[i]:
                    continue;
                if candidates[i] > rem_trg:
                    return
                curr_nums.append(candidates[i])                 
                if rem_trg == candidates[i]:   
                    res.append(curr_nums.copy())
                    curr_nums.pop()
                    return
                dfs(i+1, curr_nums, rem_trg - candidates[i])
                curr_nums.pop()

        dfs(0, [], target)
        return res