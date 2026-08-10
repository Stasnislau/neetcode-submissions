from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        full_list = [beginWord, *wordList]
        for i in range(len(full_list)):
            for j in range(i + 1, len(full_list)):
                diff = 0
                for c1, c2 in zip(full_list[i], full_list[j]):
                    if c1 != c2:
                        diff += 1
                if diff == 1:
                    g[full_list[i]].append((full_list[j]))
                    g[full_list[j]].append((full_list[i]))

        def bfs():
            q = deque([beginWord])
            actions = 0
            visited = {beginWord}
            while q:
                actions += 1
                for _ in range(len(q)):
                    item = q.popleft()
                    if item == endWord:
                        return actions
                    for nei in g[item]:
                            if not nei in visited:
                                q.append(nei)
                                visited.add(nei)
            return 0
        return bfs()
                
                                       



