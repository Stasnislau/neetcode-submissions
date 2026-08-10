class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for i in range(len(pairs)):
            time = (target - pairs[i][0])/pairs[i][1]
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)   






            
