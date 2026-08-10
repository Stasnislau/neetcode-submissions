from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for ticket_fr, ticket_to in tickets:
            adj[ticket_fr].append(ticket_to)            
        for key in adj.keys():
            adj[key].sort(reverse=True)

        path = []
        def dfs(start):
            while len(adj[start]) > 0:
                nei = adj[start].pop()
                dfs(nei)
            path.append(start)

        dfs('JFK')
        return path[::-1]

