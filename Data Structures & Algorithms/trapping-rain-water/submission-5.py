class Solution:
    def trap(self, height: List[int]) -> int:
        left, total, right = 0, 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]

        if len(height) == 0:
            return 0;
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                total += leftMax - height[left]
            else: 
                right -= 1
                rightMax = max(rightMax, height[right])
                total += rightMax - height[right]

        return total           

            
