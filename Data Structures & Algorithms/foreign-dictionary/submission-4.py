from collections import defaultdict, deque
from typing import List
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        indegree = {}
        for i in range(len(words)):
            for c in words[i]:
                indegree[c] = 0
                adj[c] = set()

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word1), len(word2))
            j = 0
            while j < min_len:
                if word1[j] != word2[j]:
                    if  word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
                j += 1
            if j == min_len and len(word1) > len(word2):
                return ''
        res = []
        q = deque()
        print(adj, indegree, res)

        for key, val in indegree.items():
            if val == 0:
                q.append(key)
        while q:
            item = q.popleft()
            for nei in adj[item]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            res.append(item)
        if len(res) != len(list(adj.keys())):
            return ''
        return "".join(res)


        
