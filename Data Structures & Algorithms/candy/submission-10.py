class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        ratings = [0] + ratings + [0]
        res = [1] * (n + 2)
        res[0] = 0
        res[n+1] = 0
        for i in range(1, n+1):
            if ratings[i] > ratings[i-1]:
                if res[i] <= res[i-1]:
                    res[i] = res[i-1] + 1
        for i in range(n, 0, -1):
            if ratings[i] > ratings[i+1]:
                if res[i] <= res[i+1]:
                    res[i] = res[i+1] + 1
        return sum(res)