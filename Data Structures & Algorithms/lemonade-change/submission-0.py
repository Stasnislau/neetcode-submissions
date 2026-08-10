class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        available = {
            5: 0,
            10: 0,
            20: 0
        }
        for bill in bills:
            available[bill] += 1
            change = bill - 5
            while change > 0:
                if change >= 10 and available[10] > 0:
                    available[10] -= 1
                    change -= 10
                else:
                    if available[5] == 0:
                        return False
                    change -= 5
                    available[5] -= 1
                    

        return True