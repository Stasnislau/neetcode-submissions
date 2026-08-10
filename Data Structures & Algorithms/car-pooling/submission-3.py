class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0] * 1001
        for p, t_s, t_e in trips:
            road[t_s] += p
            road[t_e] -= p
        curr = 0
        for i in range(1001):
            curr += road[i]
            if curr > capacity:
                return False
        return True