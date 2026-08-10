class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = len(flowerbed)
        count = 0
        if k == 1:
            if flowerbed[0] == 1:
                return n == 0
            else:
                return n <= 1
        for i in range(k):
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if not flowerbed[i+1]:
                    flowerbed[i] = 1
                    count += 1
            elif i == k - 1:
                if not flowerbed[i-1]:
                    flowerbed[i] = 1
                    count += 1
            else:
                if not flowerbed[i+1] and not flowerbed[i-1]:
                    flowerbed[i] = 1 
                    count += 1
        return count >= n

