class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        i = m - 1
        j = len(nums2) - 1
        while i >= 0 or j >= 0:
            if j < 0:
                return
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[end] = nums1[i]
                end -= 1
                i -= 1
            else:
                nums1[end] = nums2[j]
                end -= 1
                j -= 1
            
        





