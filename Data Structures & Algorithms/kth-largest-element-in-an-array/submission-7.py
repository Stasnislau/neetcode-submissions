class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) -k

        def partition(left, right):
            pivot = nums[right]
            p = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[right] = pivot, nums[p]
            return p
        left = 0
        right = len(nums) - 1
        res = 0
        while left <= right:
            res = partition(left, right)
            if res == k:
                return nums[res]
            elif res < k:
                left = res + 1
            else: 
                right = res - 1


        return 0

            
