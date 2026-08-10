class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stone = stones[0]
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            new_stone = stone2 - stone1
            heapq.heappush(stones,new_stone * -1)

        return new_stone