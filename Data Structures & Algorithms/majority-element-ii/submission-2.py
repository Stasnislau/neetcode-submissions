class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if len(nums) < 3:
            return list(set(nums))
        cand1 = 0
        count1 = 0
        cand2 = 0
        count2 = 0
        for num in nums:
            if count1 == 0:
                cand1 = num
                count1 = 1
            elif cand1 == num:
                count1 += 1
                if count2 > 0:
                    count2 -= 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            elif cand2 == num:
                count2 += 1
            else:
                count1 = max(count1 -1, 0)
                count2 = max(count2 -1, 0)
        count1 = 0
        count2 = 0
        print(cand1, cand2)
        for num in nums:
            if num == cand1:
                count1 += 1
            if num == cand2:
                count2 += 1
        res = []
        if count1 > n / 3:
            res.append(cand1)
        if count2 > n / 3:
            res.append(cand2)
        return res

