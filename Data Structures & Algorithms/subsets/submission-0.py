class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(i, current_subset):
            if i >= len(nums):
                result.append(current_subset.copy())
                return 
            current_subset.append(nums[i])
            dfs(i + 1, current_subset)

            current_subset.pop()
            dfs(i + 1, current_subset)
        dfs(0, [])

        return result

