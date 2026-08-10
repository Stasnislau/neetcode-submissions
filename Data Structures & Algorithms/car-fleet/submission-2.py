class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = {}
        for pos, sp in zip(position, speed):
            times[(pos, sp)] = (target - pos)/sp
        
        times = sorted(list(times.items()))
        stack = [times[-1][1]]
        print(times)
        for i in range(len(times) - 1, -1, -1):
            print(times[i], stack[-1] > times[i][1])
            if stack[-1] < times[i][1]:
                stack.append(times[i][1])
        
        return len(stack)   






            
