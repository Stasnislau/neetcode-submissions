class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        prev = None
        curr = None
        curr_max = 0
        total_max = 0
        for i in range(len(nums) - 1):
            prev = curr
            curr = nums[i] < nums[i+1]
            if nums[i] == nums[i+1]:
                curr = None
                curr_max = 0
                continue
            if prev != curr:
                curr_max += 1
                total_max = max(curr_max, total_max)
            else:
                curr_max = 1
        return total_max + 1