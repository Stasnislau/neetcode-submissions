class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_adj = defaultdict(int)
        out_adj = defaultdict(int)
        for trust_out, trust_in in trust:
            in_adj[trust_in] += 1
            out_adj[trust_out] += 1
        for k in range(n + 1):
            if in_adj.get(k) == n - 1 and k not in out_adj:
                return k
        return -1