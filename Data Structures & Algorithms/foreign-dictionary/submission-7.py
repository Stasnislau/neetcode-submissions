from collections import defaultdict, deque
from typing import List
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        degree = {}
        if len(words) == 1:
            return "".join(list(set(words[0])))
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            i = 0
            size = min(len(word1), len(word2))
            diff = False
            while i < size:
                c1 = word1[i]
                c2 = word2[i]
                if c1 not in degree:
                    degree[c1] = 0
                if c2 not in degree:
                    degree[c2] = 0
                if c1 != c2 and not diff:
                    if c1 in adj[c2]:
                        return ""
                    if c2 not in adj[c1]:
                        degree[c2] += 1
                    adj[c1].add(c2)
                    diff = True
                i += 1
            if not diff and len(word1) > len(word2):
                return ''
        res = []
        q = deque()
        visited = set()
        print(adj, degree)
        for key in degree.keys():
            if degree[key] == 0:
                q.append(key)
                visited.add(key)
                res.append(key)
        while q:
            item = q.popleft()
            for child in adj[item]:
                if child not in visited:
                    degree[child] -= 1
                    if degree[child] == 0:
                        q.append(child)
                        visited.add(child)
                        res.append(child)
        print(degree)
        return "".join(res) if max(degree.values()) == 0 else ''
        


        
