class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            total = 0
            visited.add(n)
            while n != 0:
                dig = n % 10
                total += dig**2
                n = n // 10
            if total in visited:
                return False
            else:
                n = total
        return True
