class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost = sum(cost)
        curr_sum = 0
        l = 0
        r = 0
        n = len(gas)
        curr_val = gas[0]
        required_val = cost[0]
        while l < len(gas):
            print(curr_val, required_val, l, r)
            if curr_val >= total_cost:
                return l
            if required_val > curr_val:
                curr_val -= gas[l]
                required_val -= cost[l]
                l += 1
            else:
                r += 1
                r_in = r % n
                curr_val += gas[r_in]
                required_val += cost[r_in]
        return -1

            


        
        

        
