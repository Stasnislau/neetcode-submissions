class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 <= 0:
                count1 = 1
                cand1 = num
            elif count2 <= 0:
                count2 = 1
                cand2 = num
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        res = []
        if count1 > len(nums) / 3:
            res.append(cand1)
        if count2 > len(nums) / 3:
            res.append(cand2)
        return res


