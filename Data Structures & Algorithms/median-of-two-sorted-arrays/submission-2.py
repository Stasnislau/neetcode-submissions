class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        totalLen = len1 + len2
        half = (totalLen + 1) // 2
        A = nums1
        B = nums2
        if len1 > len2:
            A = nums2
            B = nums1

        l = 0
        r = len(A)
        res = []
        while l <= r:
            i = (l + r) // 2
            j = half - i
            AL = A[i - 1] if i > 0 else float('-inf')
            AR = A[i] if i < len(A) else float('inf')
            BL = B[j - 1] if j > 0 else float('-inf')
            BR = B[j] if j < len(B) else float('inf')
            if AL <= BR and AR >= BL:
                if totalLen % 2 != 0:
                    return max(AL, BL)
                return (max(AL, BL) + min(AR, BR)) / 2
            elif AL > BR:
                r = i - 1
            else:
                l = i + 1
        
