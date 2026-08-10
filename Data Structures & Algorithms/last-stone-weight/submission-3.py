class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)
        new_stone = stones[0]
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            new_stone = -1 * abs(abs(stone1) - abs(stone2))
            heapq.heappush(stones,new_stone)

        return abs(new_stone)