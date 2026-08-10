class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] > abs(ast):
                    break
                elif stack[-1] == abs(ast):
                    stack.pop()
                    break
                else:
                    stack.pop()
                
            else:
                stack.append(ast)

        return stack
