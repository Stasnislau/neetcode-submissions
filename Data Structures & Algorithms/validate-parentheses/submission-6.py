class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            elif len(stack) > 0 and (ord(s[i]) - ord(stack[len(stack) - 1]) == 1 or ord(s[i]) - ord(stack[len(stack) - 1]) == 2):
                stack.pop(len(stack) - 1)
            else:
                return False
        return True if len(stack) == 0 else False