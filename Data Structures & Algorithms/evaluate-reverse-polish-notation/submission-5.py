import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(['+', '-', '*', '/'])
        stack = []
        for t in tokens:
            if t in operations:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if t == '+':
                    result = op1 + op2
                elif t == '-':
                    result = op1 - op2
                elif t == '*':
                    result = op1 * op2
                else:
                    result = math.trunc(op1/op2)
                    print(op1, op2,result )

                stack.append(result)
            else:
                stack.append(t)
        print(stack)
        return int(stack[-1])
                