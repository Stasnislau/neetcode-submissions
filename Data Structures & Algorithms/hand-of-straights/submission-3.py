from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]
            if count[first] == 0:
                heapq.heappop(heap)
                continue
            for i in range(first, first + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1

        return True