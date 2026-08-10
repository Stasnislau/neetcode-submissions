class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        pivot = len(nums) // 2
        left = []
        mid = []
        right = []
        for el in nums:
            if el < nums[pivot]:
                left.append(el)
            elif el > nums[pivot]:
                right.append(el)
            else:
                mid.append(el)
        return self.sortArray(left) + mid + self.sortArray(right)
