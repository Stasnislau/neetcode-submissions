from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for ticket_fr, ticket_to in tickets:
            adj[ticket_fr].append(ticket_to)            
        for key in adj.keys():
            adj[key].sort(reverse=True)
        outdegree = defaultdict(int)
        for source, targets in adj.items():
            for target in targets:
                outdegree[source] += 1

        path = []
        def dfs(start):
            while outdegree[start] > 0:
                nei = adj[start][outdegree[start] - 1] 
                outdegree[start] -= 1
                dfs(nei)
            path.append(start)

        dfs('JFK')
        return path[::-1]

