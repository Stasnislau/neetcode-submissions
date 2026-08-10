class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        print(people)
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                r -= 1
                res += 1
        return res