class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        point = 0
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        if nums[0] > nums[r]:
            l = 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < nums[mid - 1]:
                    point = mid
                    break
                elif nums[mid] < nums[0]:
                    r = mid - 1
                else: 
                    l = mid + 1
        if nums[len(nums) - 1] >= target:
            l = point
            r = len(nums) - 1
        else:
            l = 0
            r = point - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1 


        