class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while l <= r:
            mid = (l + r) // 2
            is_to_left = False
            is_to_right = False
            if mid > 0:
                is_to_left = nums[mid] == nums[mid - 1]
            if mid < len(nums) - 1:
                is_to_right = nums[mid] == nums[mid + 1]
            if not is_to_left and not is_to_right:
                return nums[mid]
            elif (mid - int(is_to_left) ) % 2 or (is_to_right and mid % 2):
                r = mid - 1
            else:
                l = mid + 1
        return -1
