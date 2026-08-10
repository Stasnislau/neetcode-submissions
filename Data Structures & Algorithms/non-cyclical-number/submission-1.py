class Solution:
    def isHappy(self, n: int) -> bool:
        def get_res(n):
            total = 0
            while n != 0:
                dig = n % 10
                total += dig**2
                n = n // 10
            return total
        slow = n
        fast = get_res(n)
        while slow != fast or fast != 1:
            fast = get_res(get_res(fast))
            slow = get_res(slow)
            if fast == 1:
                return True
            if slow == fast:
                return False
           
        return True
