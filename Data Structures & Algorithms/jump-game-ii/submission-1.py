class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_dist = 0
        jumps = 0
        r = 0
        for i in range(len(nums) - 1):
            if i > max_dist:
                return 0
            max_dist = max(max_dist, i + nums[i])
            if i == r:
                jumps += 1
                r = max_dist
        return jumps
