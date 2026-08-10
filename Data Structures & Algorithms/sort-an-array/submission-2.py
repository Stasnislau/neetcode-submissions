class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        buckets_n = len(nums)
        buckets = [[] for _ in range(buckets_n)]
        max_num = max(nums)
        min_num = min(nums)
        normalized = (max_num - min_num)
        if normalized == 0:
            return nums

        for num in nums:
            index = (num - min_num) * (buckets_n -1) // normalized
            buckets[index].append(num)
        total = []
        for bucket in buckets:
            total += self.insert_sort(bucket)
        return total

    def insert_sort(self, nums):
        for i in range(1, len(nums)):
            j = i - 1
            temp = nums[i]
            while j >= 0 and nums[j] > temp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j + 1] = temp
        return nums