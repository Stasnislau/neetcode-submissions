class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, tp in enumerate(temperatures):
            while stack and stack[-1][0] < tp:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([tp, i])
        return res

            