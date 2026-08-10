from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        maxVal = max(counter.values())

        buckets = [[] for _ in range(maxVal + 1)]
        
        for num in counter:
            buckets[counter[num]].append(num)
        result = []
        for index in range(len(buckets) -1, -1, -1):
            result.extend(buckets[index])

            if len(result) >= k:
                return result[:k]
