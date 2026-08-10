from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        linked = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            in_degree[dst] += 1
            linked[src].append(dst)
        
        q = deque([])

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        finish = 0
        while q:
            item = q.popleft()
            finish += 1
            for nei in linked[item]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
            
        return finish == numCourses