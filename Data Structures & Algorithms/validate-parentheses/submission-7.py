class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parents = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in parents:
                if stack and stack[-1] == parents[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack