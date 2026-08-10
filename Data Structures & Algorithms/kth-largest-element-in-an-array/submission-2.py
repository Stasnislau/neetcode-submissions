class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[right]
            p = left
            for i in range(p, right):
                if nums[i] <= pivot:
                    temp = nums[i]
                    nums[i] = nums[p]
                    nums[p] = temp
                    p += 1
            temp = nums[p] 
            nums[p] = nums[right]
            nums[right] = temp
            return p

        target = len(nums) - k
        left = 0
        right = len(nums) - 1
        res =  partition(left, right)

        while left <= right:
            if target == res:
                return nums[res]
            if res > target:
                res = partition(left, res - 1)
            else:
                res = partition(res + 1, right)



        return 0

            
