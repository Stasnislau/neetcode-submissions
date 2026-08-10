from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        maxVal = max(counter.values())

        buckets = [[] for _ in range(maxVal + 1)]

        for cnt in counter:
            buckets[counter[cnt]].append(cnt)
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                result.extend(buckets[i])
            
            if len(result) >= k:
                return result[:k];


            
        