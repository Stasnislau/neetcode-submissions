class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_pos_mono = True
        is_neg_mono = True
        prev = nums[0]
        for num in nums:
            if prev < num:
                is_neg_mono = False
            if prev > num:
                is_pos_mono = False
            prev = num
        return is_pos_mono or is_neg_mono