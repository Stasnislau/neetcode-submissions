class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        prefix = [0] * (len(height))
        postfix = [0] * (len(height))
        for i in range(1, len(height) - 1):
            print(i)
            prefix[i] = max(prefix[i-1], height[i-1])
        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(postfix[i+1], height[i+1])
        print(prefix, postfix)
        for i, h in enumerate(height):
            area += max(0,(min(prefix[i], postfix[i]) - h))
        return area

        