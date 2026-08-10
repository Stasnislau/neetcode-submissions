from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        full_list = [beginWord, *wordList]
        for word in full_list:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                g[pattern].append(word)
        steps = 0
        q = deque([beginWord])
        visited = {beginWord}
        while q:
            steps += 1
            for _ in range(len(q)):
                item = q.popleft()
                if item == endWord:
                    return steps

                for i in range(len(item)):
                    pattern = item[:i] + '*' + item[i+1:]
                    for nei in g[pattern]:
                            if nei not in visited:
                                q.append(nei)
                                visited.add(nei)
        return 0


