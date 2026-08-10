from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        links = [[] for _ in range(numCourses) ]
        for src, dst in prerequisites:
            indegree[dst] += 1
            links[src].append(dst)
        print(links, indegree)

        q = deque([])
        res = deque([])
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                res.append(i)
        print(res)
        while q:
            item = q.popleft()
            for link in links[item]:
                indegree[link] -= 1
                if indegree[link] == 0:
                    q.append(link)
                    res.appendleft(link)

        return list(res) if len(list(res)) == numCourses else []

        
