class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        seen = {}
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                seen[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        return [seen.get(num) if seen.get(num) else -1 for num in nums1]