class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr_nums):
            curr_sum = sum(curr_nums)
            print(curr_sum)
            if curr_sum == target:
                res.append(curr_nums.copy())
                return
            if curr_sum > target or i >= len(nums):
                return
            curr_nums.append(nums[i])
            dfs(i, curr_nums)

            curr_nums.pop()
            dfs(i + 1, curr_nums)
        dfs(0, [])
        return res
