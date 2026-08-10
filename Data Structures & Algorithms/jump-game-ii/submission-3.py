class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_distance = 0
        r = 0
        jumps = 0
        for i in range(len(nums) - 1):
            max_distance = max(max_distance, nums[i] + i)
            if i == r:
                r = max_distance
                jumps += 1
        return jumps