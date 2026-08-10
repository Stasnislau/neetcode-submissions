class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_on = 1
        right = len(digits) - 1
        while carry_on:
            if right == -1:
                return [1] + digits
            if digits[right] == 9:
                digits[right] = 0
            else:
                digits[right] += carry_on
                carry_on = 0
            right -= 1
        return digits
