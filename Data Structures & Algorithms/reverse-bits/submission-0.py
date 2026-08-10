class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        for i in range(32):
            bit = n & 1
            bit = bit << 31 - i 
            count = count | bit
            n = n >> 1

        return count