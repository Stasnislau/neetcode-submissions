class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False
        
        def backtrack(i, curr_arr):
            if i == len(matchsticks):
                return all(el == 0 for el in curr_arr)
                    
                
            for j in range(4):
                if curr_arr[j] - matchsticks[i] >= 0:
                    curr_arr[j] -= matchsticks[i]
                    if backtrack(i+1, curr_arr):
                        return True
                    curr_arr[j] += matchsticks[i]
            return False
        return backtrack(0, [target] * 4)  
