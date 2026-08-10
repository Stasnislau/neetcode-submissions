class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_candidate = nums[0]
        count = 1
        for i, num in enumerate(nums[1:]):
            if count == 0:
                curr_candidate = num
            if curr_candidate == num:
                count += 1
            else:
                count -= 1

        return curr_candidate

        