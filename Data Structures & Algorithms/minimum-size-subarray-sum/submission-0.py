class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curr_val = nums[0]
        min_val = float('inf')
        while l < len(nums):
            if curr_val < target and r < len(nums)-1:
                r += 1
                curr_val += nums[r]
            elif curr_val >= target:
                print(r,l,curr_val, r - l + 1)
                min_val = min(r - l + 1, min_val)
                curr_val -= nums[l]
                l += 1
            else:
                return min_val if min_val != float('inf') else 0   
        return min_val if min_val != float('inf') else 0              