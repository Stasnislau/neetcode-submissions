class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        for i in range(32):
            count = count | ((n & 1) << 31 - i)
            n = n >> 1

        return count