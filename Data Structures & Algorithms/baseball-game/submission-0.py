class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == '+':
                first = stack[-2]
                second = stack[-1]
                stack.append(first + second)
                res += first + second
            elif op == 'C':
                val = stack.pop()
                res -= val
            elif op == 'D':
                val = stack[-1]
                stack.append(val*2)
                res += val * 2
            else:
                res += int(op)
                stack.append(int(op))
        return res