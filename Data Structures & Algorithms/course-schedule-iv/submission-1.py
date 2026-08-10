class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        out_adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        reqs = [set() for _ in range(numCourses)]
        for req, course in prerequisites:
            out_adj[req].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            item = q.popleft()
            for child in out_adj[item]:
                reqs[child].add(item)
                reqs[child] = reqs[child] | reqs[item]
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)


        res = []
       
        for query_child, query_par in queries:
            res.append(query_child in reqs[query_par])
        return res

