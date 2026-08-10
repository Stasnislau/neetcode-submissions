class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        sums = set({0})
        for num in nums:
            temp = sums.copy()
            for el in temp:
                curr_sum = el + num
                if curr_sum <= target:
                    if curr_sum == target:
                        return True
                    sums.add(curr_sum)
            sums.add(num)
          
        
        return False
