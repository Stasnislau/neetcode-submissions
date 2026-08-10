from collections import defaultdict, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num_of_types = Counter(tasks)
        freqs = list(num_of_types.values())
        max_freq = max(freqs)
        num_of_max_freq = sum(1 for c in freqs if c == max_freq)
        return max(len(tasks), (max_freq - 1 ) * (n + 1) + num_of_max_freq)



