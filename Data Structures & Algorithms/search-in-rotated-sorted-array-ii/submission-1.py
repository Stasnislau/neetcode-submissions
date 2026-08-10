class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[r]:
                l += 1
                continue
            if nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1


            
        return False