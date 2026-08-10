class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(j, current_set):
            if j >= len(nums):
                result.append(current_set.copy())
                return 
            current_set.append(nums[j])
            dfs(j + 1, current_set)
            current_set.pop()

            dfs(j + 1, current_set)

        dfs(0, [])
        return result

