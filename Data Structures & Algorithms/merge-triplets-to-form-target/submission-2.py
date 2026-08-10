class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f_good = False
        s_good = False
        t_good = False
        for trp in triplets:
            if trp[0] > target[0] or trp[1] > target[1] or trp[2] > target[2]:
                continue
            if trp[0] == target[0]:
                f_good = True
            if trp[1] == target[1]:
                s_good = True
            if trp[2] == target[2]:
                t_good = True
            
        return f_good and s_good and t_good